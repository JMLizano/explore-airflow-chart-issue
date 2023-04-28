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
        lib_method()
        time.sleep(10)
    
    @dag.task(task_id=f"second_task")
    def second_function():
        print("Failed in previous task")

    sleeping_task = my_sleeping_function()
    second_task = second_function()

    sleeping_task > second_task
