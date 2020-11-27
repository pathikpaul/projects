
from datetime import timedelta,datetime

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Pathik',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG(
    'pathik-tutorial',
    default_args=default_args,
    start_date = datetime(2020,11,27),
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)
t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag)
t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command='echo HelloWorld',
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t1 >> [t2, t3]
