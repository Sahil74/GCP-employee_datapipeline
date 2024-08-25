# Employee Data ETL Pipeline

## Overview

This project implements a comprehensive ETL (Extract, Transform, Load) pipeline for employee data, 
leveraging Google Cloud technologies. The pipeline automates the process of extracting data with Python, 
transforming and loading it into BigQuery using Data Fusion, and visualizing it in Looker Studio. 
Apache Airflow manages and schedules the entire workflow.

## Architecture
![Data Visualization](./images/visualization.png)

## Workflow

- Data Extraction: Extract employee data using a Python script and upload it as CSV files to Google Cloud Storage.
- Data Transformation: Use Google Cloud Data Fusion to transform the data, including cleaning and enrichment.
- Data Loading: Load the transformed data into BigQuery for structured storage and analysis.
- Data Visualization: Create interactive reports and dashboards in Looker Studio using the BigQuery dataset.
- Automation: Manage and automate the ETL pipeline with Apache Airflow (Cloud Composer).

