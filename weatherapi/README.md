# Using Weather API

## Prerequisites :: Obtain API Key from 
https://openweathermap.org/api

## Install Python 
```bash
sudo yum install -y python3
sudo pip3 install virtualenv
python3 -m virtualenv venvproj
. ~/venvproj/bin/activate
$ pip3 install requests
$ pip3 install numpy
```

## Prerequisites :: install and Configure MySQL
Details : pathikpaul/projects/MySQL.txt
```bash
$ python3 createWeatherTable.py
  This will create the "weather_table"
```

## Get Data from API to Local File
```bash
$ mkdir -p ~/projects/weatherapi/data
$ python3 getWeather.py
data/2020-11-27.json
$ cat data/2020-11-27.json
{"coord": {"lon": -74.41, "lat": 40.52}, "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}], "base": "stations", "main": {"temp": 284.52, "feels_like": 282.64, "temp_min": 284.15, "temp_max": 284.82, "pressure": 1017, "humidity": 81}, "visibility": 10000, "wind": {"speed": 2.1, "deg": 290}, "clouds": {"all": 1}, "dt": 1606450436, "sys": {"type": 1, "id": 4686, "country": "US", "sunrise": 1606391835, "sunset": 1606426404}, "timezone": -18000, "id": 5097529, "name": "Edison", "cod": 200}
```

## Load Data from Local File to MySQL
```bash
$ python3 loadWeather.py
```

## config.py
API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MYSQL_HOST="192.168.77.10"
MYSQL_USER="newuser"
MYSQL_PASSWORD="Chase901#"
MYSQL_DATABASE="dbone"

