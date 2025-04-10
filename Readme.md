### About Me 

My name is Mike Cancell (https://www.linkedin.com/in/mikecancell/). If you’re visiting this repository, it’s likely because you want to evaluate my current Python skills. This repo will give you some insight into my capabilities. 

I’m still a novice in Python, but I’m learning more each day. On the other hand, I possess strong SQL skills. If you're interested in reviewing my previous SQL work, please reach out to me via LinkedIn. 

While I don't have a public repository for my SQL work due to it being actual in-production code, I’m willing to share some code samples if you're seriously considering hiring me. The shared code will not contain any sensitive data, so you’ll be able to see how I model financial data and process KPIs without exposing any actual company information.

## My Local Dev Env
While I may move code back to my cloud VM, I am currently working locally on a Windows laptop to avoid costs. I do maintain a cloud instance on GCP, but it is currently idle to minimize monthly expenses.
### Env Requirements
See the Requirements.txt file for the list of lib dependencies. (I try to Freeze the Reqs file regularly.)
### Code Deployment
Right now, I am not using Docker, Kubernetes, etc. for code deployment. I may try that as an excercise in the future. But as of now, I am just using VS Code with a local env.
### AI Coding
I’m a Python novice/journeyman ;-). While I code SQL by hand without any AI assistance, I am now using AI—specifically Co-Pilot—for Python, and I absolutely love it! 

Has AI changed my coding experience? Yes, it has. It's helping me quickly navigate the vast array of Python libraries. I'm new to using AI for coding; I used to spend a lot of time hand-coding in JavaScript and other non-native languages. SQL is my native language, although I was once a C programmer at Bell Labs—back in the horse-and-buggy days (don't ask...).

Here’s the takeaway: using AI is not a crutch, in my opinion. You still need to understand programming tasks to ask the right questions. When it comes to Python, that's exactly what I focus on. 
## Project Goals
The goal of the project is to demonstrate the typical types of pipelines and workflows that are performed when working with diffent types of Datasets. 
Thus, while there are some algorythimic examples within the different pipelines, the main purpose about working with data. 
## Common aspects
### Parallization
You will find that in many pipelines, parallization is used to increase performance of certain operations, e.g., web scraping. Please see the concurrent.futures lib data re: Launching parallel tasks -https://docs.python.org/3/library/concurrent.futures.html
### Memory Optimization
Whenever appropriate, buffering is used so that Dataframe loading does not hit memory issues. For example, in the Taxi Trip Dataset, it is possible to load >1M rows without running out of memory. Sometimes, I use Pandas, and sometimes I use Polars. But regardless, attention is paid to potential memory issues. 
### Progress and Status Reporting
The tqdm (https://pypi.org/project/tqdm/) lib is used for Progress Handling
### Caching 
Pickle Files (https://docs.python.org/3/library/pickle.html) are used to cache dataframes. They are used to both to prevent re-calling operations, e.g., whois, screenscraping meta tags, etc. and they are used for downstream workflows, e.g., Load Data from Internet (JSON) ...and pickle, Clean and Transformdata ...and pickle, Load db tables, etc. 
### File Compression
Insofar as large datasets are ingested from Internet, local data is often stored in compressed format, e.g., zip. Likewise, when reading, data is often read from within the compressed file (e.g., w/out decompressing first).
## Background and History
I created this repo in Dec 2024. It was around that time that I got caught up in a force reduction at my former company, Interactions Corp. This repo basically represents my journey to learn how to utilize Python for ETL and ML.
## Future Direction
After I exhaust each dataset, in terms of what could be analyzed from the data. I move on to another dataset. But I am confined to *free* sources, iow I am not paying for data, e.g., D&B, etc. So all datasets are of the 'Beg, Borrow, and Steal' variety. 
### Orchestration and Deployment
As of date of this writing, I am not using any orchestration tools (Airflow, NiFi, Dagster, etc.) I hope to start adding workflow deployment in the future.
# Project Organization
Project is organized by Dataset, with set having directories for Extract, Transform, Load, Analyze, (and Orchestrate tbd)
## Common
This area contains common code, credentials, etc. which pertain across all Datasets
### Functions
As I develop new functions that are used within a given Dataset, I will be abstracting and migrating to this area, as apprpropriate. 
### Credentials
This area contains credential data like API keys, IAM credentials, logon credentials, etc. There is a .gitignore to prevent any sensitive credentials from getting upload to the repo.
### .Pickles
I use pickle files for local caching. .pkl files are ignored by Git and thus not uploaded.
(If your not familiar with pickle usage or rationale, please see https://docs.python.org/3/library/pickle.html for details.)
## Dataset
Operations for Each Dataset are self-contain contained with subdirectories for typlical ETL Operations
### Common Dir
This area will be used for functions, classes, etc that may be specific to the respective Dataset

### Credentials
Dataset specific Credentials may be stored here or off the project's root. But note, all credential data is git ignored.
### .pickles
This area is used to cache dataframes specific to the respective Dataset. Note again, that all .pkl files are git ignored.
### Extract
This area is where Data ingestion routines are stored. This corresponds to Extract pipelines used to ingest data from various sources.  
### Transform
This area contains the various pipelines for data cleaning, arrangement (e.g., semantic modeling, schema), ML learning for (time series regression, categorization, entity resolution, etc.)
Once Dataframes are fully formulared they are pickled for caching and downstream operations, e.g., loading to a cloud DB, etc.
### Load
This area containes the pipelines for loading data to a landing area, e.g., clould tables, datamart, etc.
### Query
This area contains SQL code that works on the Loaded Tables to Materialize Datasets for ultimate reporting/visulaization. 