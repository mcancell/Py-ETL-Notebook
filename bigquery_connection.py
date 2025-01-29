from google.cloud import bigquery

def run_query(query):
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Run the query and get the results.
    query_job = client.query(query)
    results = query_job.result()

    # Print the results.
    for row in results:
        print(row)

if __name__ == "__main__":
    query = """
    SELECT *
    FROM `your-project.your_dataset.your_table`
    LIMIT 10
    """
    run_query(query)
