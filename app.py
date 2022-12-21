from flask import Flask, render_template, redirect, request
import requests
import json

app=Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        print(user_input)

        #user_input = 'delhi'
        complete_api_link1 ="http://api.openweathermap.org/geo/1.0/direct?q="+user_input+"&limit=5&appid=52e40abca47fa344472973b265b5c319"
        location = requests.get(complete_api_link1)
        #print(location.status_code)
        loc = location.json()
        #print(location.text)
        lat = str(loc[2]['lat'])
        lon = str(loc[2]['lon'])
        complete_api_link ="https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=52e40abca47fa344472973b265b5c319"
        a = requests.get(complete_api_link)
        data = a.json()
        #print(a.status_code)
        #print(data)
        temp = data['main']['temp']


        return render_template("index.html", temp=temp)
    else:
        return render_template('index.html')

    





if __name__ =="__main__":
    app.run(debug=False, port=8000)