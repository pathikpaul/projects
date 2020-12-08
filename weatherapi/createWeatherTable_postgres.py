import psycopg2
conn = psycopg2.connect(host='192.168.77.11',user='samplerole',password='NewPassword',database='testdb')
curr = conn.cursor()
tablename = 'weather_table'
create_table = """ create table if not exists %s (
city TEXT, country TEXT, latitude REAL, longitude REAL, todays_date DATE, humidity REAL, pressure REAL, min_temp REAL, max_temp REAL, temp     REAL, weather  TEXT)""" % tablename
curr.execute(create_table)
conn.commit()
conn.close()
