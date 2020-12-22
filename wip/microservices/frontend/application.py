import json
#import flask
#import platform
#import socket
#from datetime import datetime
#from flask import Flask,render_template,request,abort,redirect,url_for
#import os.path
#import sys
import requests
from flask import Flask,render_template,redirect,url_for

application = Flask(__name__)

payload = { "username":"admin", "password":"12345" }
jwtToken = ""
ErrorMessage=""

@application.route('/moviedetails/<string:movieid>',methods=["GET"])
def get_moviedetails(movieid):
    global ErrorMessage
    r = requests.get("http://192.168.77.10:5001/movies/"+movieid, headers={'Authorization': 'Bearer '+jwtToken})
    if r.status_code != 200:
       print(type(r.text),r.text)
       print(r.text)
       ErrorMessage=r.text
       ErrorMessage="Hello world"
       return redirect(url_for('welcome'))
    print(r)
    jj = json.loads(r.text)
    return render_template("moviedetails.html",notes=jj)

@application.route('/')
def welcome():
    global ErrorMessage
    NewErrorMessage=ErrorMessage
    ErrorMessage=""
    ## Invloke Login URL to Get the token
    #r = requests.post("http://192.168.77.10:5001/movies/login",json=payload)
    #print(r)
    #jj = json.loads(r.text)
    #jwtToken = jj["jwt"]
    #print ("jwtToken=", jwtToken)
    ##
    r = requests.get("http://192.168.77.10:5002/showtimes")
    jj = json.loads(r.text)
    return render_template("welcome.html",notes=jj,message=NewErrorMessage)
if __name__ == "__main__":
    #
    ## Invloke Login URL to Get the token
    r = requests.post("http://192.168.77.10:5001/movies/login",json=payload)
    print(r)
    jj = json.loads(r.text)
    jwtToken = jj["jwt"]
    print ("jwtToken=", jwtToken)
    #
    r = requests.get("http://192.168.77.10:5001/movies/720d006c-3a57-4b6a-b18f-9b713b073f3c", headers={'Authorization': 'Bearer '+jwtToken})
    if r.status_code != 200:
       print(r.text)
       exit (1)
    print(r)
    jj = json.loads(r.text)
    for key in jj.keys():
        print(key,jj[key])
    application.run(port=5009, host= '0.0.0.0' ,debug=True)
