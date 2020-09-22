from flask import Flask, redirect, render_template
import requests, json
from flask_cors import CORS, cross_origin
app = Flask(__name__)

@app.route('/')
def home():
    # country, longitude, latitude, 
    return render_template('index.html', country='', lon='', lat='')


@app.route('/loction')
def location():
    phone_code = []
    with open('country_phone_code.json') as file:
        phone_code = file.read()
    # convert phone_code to json format
    phone_code = json.loads(phone_code)
    # get IP location
    res = requests.get('https://ipinfo.io/')
    # print data into text format
    print(res.text)
    # print data into json format
    # print(res.json())
    # convert text into json format
    json = json.loads(res.text)
    # get Country code
    # print(json['country'])
    # abstract country phone_code
    # print(phone_code[json['country']])
    print(json['country'], ':', phone_code[json['country']])