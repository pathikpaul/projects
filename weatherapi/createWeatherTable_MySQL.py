import mysql.connector
import config as C
mydb = mysql.connector.connect(host=C.MYSQL_HOST, user=C.MYSQL_USER, password=C.MYSQL_PASSWORD, database=C.MYSQL_DATABASE,  auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pet")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
tablename = 'weather_table'
create_table = """ create table if not exists %s (
city TEXT, country TEXT, latitude REAL, longitude REAL, todays_date DATE, humidity REAL, pressure REAL, min_temp REAL, max_temp REAL, temp     REAL, weather  TEXT)""" % tablename
mycursor.execute(create_table)
mydb.commit()
