import psycopg2
import numpy as np
from datetime import datetime
import os
import json
conn = psycopg2.connect(host='192.168.77.11',user='samplerole',password='NewPassword',database='testdb')
curr = conn.cursor()

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
    curr.execute(insert_cmd,row)
curr.execute("SELECT * FROM weather_table")
myresult = curr.fetchall()
for x in myresult:
  print(x)
conn.commit()
conn.close()
