import imaplib
import email
import pandas as pd
from bs4 import BeautifulSoup
from dateutil import parser
from tqdm import tqdm

def fetch_emails(credentials, since_date="01-Jan-2025"):
    """
    Fetch emails from a Gmail account since a specified date and return them as a pandas DataFrame.
    Args:
        credentials (dict): A dictionary containing Gmail credentials with keys 'gmail_credentials', 
                            'email', and 'password'.
        since_date (str, optional): The date from which to fetch emails in the format "DD-MMM-YYYY". 
                                    Defaults to "01-Jan-2025".
    Returns:
        pandas.DataFrame: A DataFrame containing email details with columns:
                          - 'Date': The date the email was sent.
                          - 'Subject': The subject of the email.
                          - 'From': The sender's email address.
                          - 'To': The recipient's email address.
                          - 'Message-ID': The unique message ID of the email.
                          - 'Body': The body content of the email.
                          - 'Reply-To': The reply-to email address.
    """

    # Extract email address and password from credentials
    email_addr = credentials['gmail_credentials']['email']
    email_pass = credentials['gmail_credentials']['password']
    
    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_addr, email_pass)

    # Select the mailbox you want to use
    mail.select('inbox')

    # Search for emails since the specified date
    status, messages = mail.search(None, f'(SINCE "{since_date}")')

    # Get the email IDs
    email_ids = messages[0].split()

    # Initialize a list to store email details
    email_details = []

    # Fetch the email data and store in the list
    for num in tqdm(email_ids, desc="Fetching emails"):
        status, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        email_info = {
            'Date': msg['date'],
            'Subject': msg['subject'],
            'From': msg['from'],
            'To': msg['to'],
            'Message-ID': msg['message-id'],
            'Body': None,
            'Reply-To': msg['reply-to']
        }
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    email_info['Body'] = part.get_payload(decode=True).decode(errors='ignore')
                    break
                elif part.get_content_type() == 'text/html':
                    html_content = part.get_payload(decode=True).decode(errors='ignore')
                    soup = BeautifulSoup(html_content, 'html.parser')
                    email_info['Body'] = soup.get_text()
                    break
        else:
            email_info['Body'] = msg.get_payload(decode=True).decode(errors='ignore')
        email_details.append(email_info)

    # Convert the list to a pandas DataFrame
    df_emails_imap = pd.DataFrame(email_details)

    # Remove any characters from the datestring that appear like this ' (*)'
    df_emails_imap['Date'] = df_emails_imap['Date'].str.replace(r'\s*\(.*?\)', '', regex=True)
    
    # Remove any date strings that end in 'GMT'
    df_emails_imap['Date'] = df_emails_imap['Date'].str.replace(r'GMT$', '', regex=True)
    
    # Convert the 'Date' column to datetime with specified format, handling timezones
    def parse_date(date_str):
        try:
            return parser.parse(date_str)
        except (parser.ParserError, TypeError):
            return pd.NaT

    df_emails_imap['Date'] = df_emails_imap['Date'].apply(parse_date)
    df_emails_imap['Date'] = pd.to_datetime(df_emails_imap['Date'], errors='coerce', utc=True)
    
    # If 'To' column is missing, set it to the email address from credentials
    df_emails_imap['To'] = df_emails_imap['To'].fillna(email_addr)
    
    # If 'Reply-To' column is missing, set it to the 'From' address
    df_emails_imap['Reply-To'] = df_emails_imap['Reply-To'].fillna(df_emails_imap['From'])
    return df_emails_imap
