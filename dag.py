from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    'employee_data',
    default_args=default_args,
    description='Run an external Python script',
    schedule_interval='@daily',
    max_active_runs=2,
    catchup=False,
)
   
with dag:
    run_script_task = BashOperator(
        task_id = 'extract_data' , 
        bash_command='python /home/airflow/gcs/dags/scripts/extract_push.py',
    )
    start_pipeline = CloudDataFusionStartPipelineOperator(
        location= 'us-central1',
        pipeline_name='etl-pipeline',
        instance_name = 'datafusion-dev',
        task_id = 'start_defusion_pipeline',
        pipeline_timeout=3600,
    )
    run_script_task >> start_pipeline