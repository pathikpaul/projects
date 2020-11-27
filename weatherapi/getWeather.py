import requests
import config as C
import json
from datetime import datetime
import os
import logging
def get_weather():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    parameters={'q': 'Edison,USA', 'appid':C.API_KEY}
    result = requests.get("http://api.openweathermap.org/data/2.5/weather?",parameters)
    if result.status_code==200:
        json_data = result.json()
        file_name = str(datetime.now().date())+'.json'
        tot_name =  os.path.join(os.path.dirname(__file__), 'data', file_name)
        print('FileName=',tot_name)
        with open(tot_name, 'w') as outputfile:
            json.dump(json_data, outputfile)
    else:
        print("Error in API call")
if __name__ == "__main__":
    get_weather()
