import datetime
import time

from airflow import DAG

from mypackage.lib.mylib import lib_method

with DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2023, 4,1),
    schedule="@daily"
) as dag:
    @dag.task(task_id=f"sleep")
    def my_sleeping_function():
        """This is a function that will run within the DAG execution"""
        lib_method()
        time.sleep(10)

    sleeping_task = my_sleeping_function()
