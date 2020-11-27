import mysql.connector
import numpy as np
from datetime import datetime
import os
import config as C
import json
mydb = mysql.connector.connect(host=C.MYSQL_HOST, user=C.MYSQL_USER, password=C.MYSQL_PASSWORD, database=C.MYSQL_DATABASE,  auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

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
#tablename = 'weather_table'
insert_cmd = """
INSERT INTO weather_table (city,country,latitude,longitude,todays_date,humidity,pressure,min_temp,max_temp,temp,weather)
VALUES                    (%s,  %s,     %s,      %s,       %s,         %s,      %s,      %s,      %s,      %s,  %s);"""
row                      =(city,country,lat,     lon,      today_dt,   humid,   press,   min_temp,max_temp,temp,weather)
if valid_data is True:
    mycursor.execute(insert_cmd,row)
mycursor.execute("SELECT * FROM weather_table")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
mydb.commit()
