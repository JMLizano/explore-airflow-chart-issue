import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

from mypackage.lib.mylib import lib_method

with DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2023, 4,1),
    schedule="@daily",
):
    EmptyOperator(task_id="task")