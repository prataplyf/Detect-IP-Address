from flask import Flask, redirect, render_template, request,url_for
import requests
import json
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
    # country, longitude, latitude,
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
        json_data = json.loads(res.text)
        # get Country code
        # print(json['country'])
        # abstract country phone_code
        # print(phone_code[json['country']])
        log_lat = json_data['loc'].split(',')
        log = log_lat[0]
        lat = log_lat[1]
        print(json_data['country'], ':', phone_code[json_data['country']])
        count = 1
        return render_template('index.html', country=json_data['country'], phone_code=phone_code[json_data['country']], log=log, lat=lat, count=count)
    else:
        return render_template('index.html', country='', phone_code='', lon='', lat='')



@app.route('/')
@app.route('/bank', methods=['POST', 'GET'])
def bank():
    if request.method == 'POST':
        ifsc = request.form['ifsc']
        print(ifsc)
        url = "https://ifsc.razorpay.com/"
        data = requests.get(url + ifsc).json()
        return render_template('index.html', data=data)
    return render_template('index.html')



@app.route('/')
@app.route('/location', methods=['POST', 'GET'])
def location():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        geolocator = Nominatim(user_agent="geoapiExercise")
        zip_location = geolocator.geocode(zipcode)
        return render_template('index.html', data=zip_location)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
