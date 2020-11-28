from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators import PythonOperator
from airflow.hooks import PostgresHook
#import mysql.connector
import numpy as np
import os
#import config as C
import json

def load_data(ds, **kwargs):
    pg_hook = PostgresHook(postgres_conn_id='weather_id')
    file_name = str(datetime.now().date())+'.json'
    tot_name =  os.path.join(os.path.dirname(__file__), 'data', file_name)
    with open(tot_name, 'r') as inputfile:
        doc = json.load(inputfile)
    city    = str(doc['name'])
    country = str(doc['sys']['country'])
    lat     = float(doc['coord']['lat'])
    lon     = float(doc['coord']['lon'])
    humid   = float(doc['main']['humidity'])
    press   = float(doc['main']['pressure'])
    min_temp= float(doc['main']['temp_min']) - 273.15
    max_temp= float(doc['main']['temp_max']) - 273.15
    temp    = float(doc['main']['temp'])     - 273.15
    weather = str(doc['weather'][0]['description'])
    today_dt= datetime.now().date()
    valid_data=True
    for valid in np.isnan([lat,lon,humid,press,min_temp,max_temp,temp]):
       if valid is False:
           valid_data=False
           break;
    insert_cmd = """
    INSERT INTO weather_table (city,country,latitude,longitude,todays_date,humidity,pressure,min_temp,max_temp,temp,weather)
    VALUES                    (%s,  %s,     %s,      %s,       %s,         %s,      %s,      %s,      %s,      %s,  %s);"""
    row                      =(city,country,lat,     lon,      today_dt,   humid,   press,   min_temp,max_temp,temp,weather)
    if valid_data is True:
        pg_hook.run(insert_cmd,parameters=row)

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
    'weatherDAG',
    default_args=default_args,
    description='Weather API DAG',
    start_date = datetime(2020,11,27),
    schedule_interval=timedelta(days=1))
t1 = BashOperator(
    task_id='get_weather',
    bash_command='python3 ~/airflow/dags/src/getWeather.py',
    dag=dag)
t2 = PythonOperator(
    task_id='transform_load',
    provide_context=True,
    python_callable=load_data,
    dag=dag)
t1 >> t2
