# Chicago Taxi Trips Project

This project analyzes the Chicago Taxi Trips dataset from BigQuery's public datasets. It includes SQL queries, Python notebooks, and visualizations to extract insights and answer business questions.

---

## Directory Structure

### **Datasets**
This directory contains the raw and processed data files used in the analysis.

- **`Chi_Taxi_Trip_Insights_Branch.ipynb`**  
  A Jupyter Notebook containing Python code for data analysis and visualization. It includes SQL queries, data processing, and insights generation.

- **`Chi_Taxi_Trip_Insights_Branch_Part_I.bqsql`**  
  A SQL file containing queries for Part I of the analysis, focusing on identifying the largest month-over-month changes in trips and fare-per-mile.

- **`Chi_Taxi_Trip_Insights_Branch_Part_II.bqsql`**  
  A SQL file containing queries for Part II of the analysis, allowing for creative exploration of the dataset to uncover additional insights.

- **`Chi_Taxi_Trip_Insights_Branch_Part_II_Extra.bqsql`**  
  A SQL file with extended queries for deeper analysis, including metrics like average speed, revenue, and trip density.

- **`Insights_Part_III.parquet`**  
  A Parquet file storing processed data for faster loading and analysis in subsequent steps.

---

### **Credentials**
This directory contains configuration files and credentials required for accessing external services.

- **`locations_conf.json`**  
  A JSON file specifying directory paths and credentials, including the BigQuery service key.

---

### **Common**
This directory contains reusable functions and utilities for the project.

- **`Functions`**  
  A subdirectory with Python scripts for common tasks like data formatting, text reformatting, and visualization.

---

## Key Files

### **Jupyter Notebook**
- **`Chi_Taxi_Trip_Insights_Branch.ipynb`**  
  The main notebook for this project. It includes:
  - Data loading and preprocessing.
  - SQL query execution using BigQuery.
  - Data visualization with Plotly.
  - Insights generation and reporting.

### **SQL Files**
- **`Chi_Taxi_Trip_Insights_Branch_Part_I.bqsql`**  
  Focuses on identifying the largest month-over-month changes in trips and fare-per-mile.

- **`Chi_Taxi_Trip_Insights_Branch_Part_II.bqsql`**  
  Explores additional insights and trends in the dataset.

- **`Chi_Taxi_Trip_Insights_Branch_Part_II_Extra.bqsql`**  
  Contains extended queries for advanced metrics and analysis.

### **Data Files**
- **`Insights_Part_III.parquet`**  
  A processed dataset saved in Parquet format for efficient loading and analysis.

---

## How to Use

1. **Setup**  
   Ensure you have the required credentials and configuration files in the `Credentials` directory.

2. **Run the Notebook**  
   Open `Chi_Taxi_Trip_Insights_Branch.ipynb` in Jupyter Notebook or JupyterLab. Follow the steps to load data, execute queries, and generate insights.

3. **Modify SQL Queries**  
   Edit the SQL files in the `Datasets` directory to customize the analysis.

4. **Save Results**  
   Save processed data to Parquet files for faster loading in future analyses.

---

## Contact

For questions or support, please contact:  
- Mike Cancell (mike.cancell@gmail.com)
- GitHub: [mikecancell](https://github.com/mcancell/Py-ETL-Notebook/tree/main/Datasets/Chicago%20Taxi%20Trips)
- LinkedIn: [Mike Cancell](https://www.linkedin.com/in/mikecancell/)