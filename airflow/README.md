# airflow
## install airflow 
```bash
sudo yum install -y python3
sudo pip3 install virtualenv
python3 -m virtualenv venvproj
sudo yum -y install gcc gcc-c++
export AIRFLOW_HOME=~/airflow
. ~/venvproj/bin/activate
sudo yum install python3-devel
pip3 install apache-airflow
## for postgres
pip3 install sqlalchemy
pip3 install psycopg2-binary
## for this example
pip3 install requests
pip3 install numpy
```

## airflow Quick Start
 - https://airflow.apache.org/docs/stable/start.html
 - airflow initdb
 - airflow webserver -p 8080
 - airflow scheduler
 - http://192.168.77.10:8080/admin/
 - airflow run example_bash_operator runme_0 2015-01-01

## airflow tutorial
 - https://airflow.apache.org/docs/stable/tutorial.html
 - https://www.applydatascience.com/airflow/writing-your-first-pipeline/
 - https://www.youtube.com/watch?v=43wHwwZhJMo
```bash
mkdir -p  ~/airflow/dags
python3 ~/projects/airflow/tutorial_2.py ##Validate that the code compiles
cp ~/projects/airflow/tutorial_2.py ~/airflow/dags/.
vi ~/airflow/dags/config.py
   API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
airflow list_dags
airflow list_tasks pathik-tutorial
airflow list_tasks pathik-tutorial --tree
airflow test       pathik-tutorial print_date 2020-11-27
airflow test       pathik-tutorial sleep 2020-11-27
airflow test       pathik-tutorial templated 2020-11-27 
airflow backfill   pathik-tutorial -s 2020-11-27 -e 2020-11-28
```

## http://michael-harmon.com/blog/AirflowETL.html
### PreReauisties: Test and Validate that the WeatherAPI code is working with postgres
### copy the code 
```bash
mkdir ~/airflow/dags
mkdir ~/airflow/dags/data
cp  ~/projects/weatherapi/weatherDAG_postgres.py ~/airflow/dags/.
find ~/airflow/dags/   
below files were created by airflow
	~/airflow/dags/__pycache__
	~/airflow/dags/__pycache__/tutorial_2.cpython-36.pyc
	~/airflow/dags/__pycache__/weatherDAG_postgres.cpython-36.pyc
 It takes a few minutes for the DAG to appear on the GUI
```
### Create Connection for postgres
  * weather_id
  * Postgres
  * Host: 192.168.77.11
  * Schema: testdb
  * Port: 5432
### Test the DAG
```bash
airflow list_dags
airflow list_tasks weatherDAG
airflow list_tasks weatherDAG --tree
airflow test weatherDAG get_weather 2020-11-27
find ~/airflow/dags/data/
airflow test weatherDAG transform_load 2020-11-27
psql --host=192.168.77.11 --port=5432 --username=samplerole --dbname=testdb
testdb=> select * from weather_table;
  city  | country | latitude | longitude | todays_date | humidity | pressure | min_temp | max_temp | temp  |  weather
--------+---------+----------+-----------+-------------+----------+----------+----------+----------+-------+-----------
 Edison | US      |    40.52 |    -74.41 | 2020-11-28  |       62 |     1016 |    10.56 |    12.78 | 11.71 | clear sky

airflow backfill weatherDAG -s 2020-11-27 -e 2020-11-28
```
