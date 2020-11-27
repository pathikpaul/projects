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
mkdir -p ~/airflow/example_dags
vi ~/airflow/example_dags/tutorial.py
python3 ~/airflow/example_dags/tutorial.py
airflow list_dags
airflow list_tasks tutorial
airflow list_tasks tutorial --tree
airflow test tutorial print_date 2015-06-01
airflow test tutorial sleep 2015-06-01
airflow test tutorial templated 2015-06-01
airflow backfill tutorial -s 2015-06-01 -e 2015-06-02
```

## http://michael-harmon.com/blog/AirflowETL.html
- copy the code 
```bash
cp  ~/projects/weatherapi/getWeather.py ~/airflow/dags/src/getWeather.py
```
- Create Connection
 - weather_id
 - mysql
 - Host: 192.168.77.10
 - Schema: dbone
 - Port: 3306
