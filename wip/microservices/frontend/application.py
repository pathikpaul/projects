import json
#import flask
#import platform
#import socket
#from datetime import datetime
#from flask import Flask,render_template,request,abort,redirect,url_for
#import os.path
#import sys
import requests
from flask import Flask,render_template

application = Flask(__name__)

@application.route('/')
def welcome():
    r = requests.get("http://192.168.77.10:5002/showtimes")
    jj = json.loads(r.text)
    return render_template("welcome.html",notes=jj)
if __name__ == "__main__":
    #r = requests.get("http://192.168.77.10:5002/showtimes")
    #jj = json.loads(r.text)
    #for key in jj.keys():
    #    print(key)
    #    for movie in jj[key]:
    #        print(movie)
    application.run(port=5009, host= '0.0.0.0' ,debug=True)
