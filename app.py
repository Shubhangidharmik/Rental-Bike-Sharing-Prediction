from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('LR_model','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_bike_count():

    Seasons_Spring = int(request.form.get('Seasons_Spring'))
    Seasons_Summer = int(request.form.get('Seasons_Summer'))
    Seasons_Winter = int(request.form.get('Seasons_Winter'))
    Holiday_No_Holiday = int(request.form.get('Holiday_No Holiday'))
    Functioning_Day_Yes = int(request.form.get('Functioning Day_Yes'))
    Hour = int(request.form.get('Hour'))
    Temperature = float(request.form.get('Temperature(°C)'))
    Humidity = int(request.form.get('Humidity(%)'))
    Wind_speed = float(request.form.get('Wind speed (m/s)'))
    Visibility = int(request.form.get('Visibility (10m)'))
    Dew_point_temperature = float(request.form.get('Dew point temperature(°C)'))
    Solar_Radiation = float(request.form.get('Solar Radiation (MJ/m2)'))
    Rainfall = float(request.form.get('Rainfall(mm)'))
    Snowfall = float(request.form.get('Snowfall (cm)'))
    month = int(request.form.get('month'))
    weekdays_weekend = int(request.form.get('weekdays_weekend'))

    # prediction
    #result = model.predict(np.array([Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature,Humidity,Wind_speed,Visibility,Dew_point_temperature,Solar_Radiation,Rainfall,Snowfall,month,weekdays_weekend]).reshape(-1,1))
    #prediction = model.predict(result)

    #return render_template('index.html', prediction_text='bike_count is {}'.format(prediction))

    # print the result

    print(model.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature,Humidity,Wind_speed,Visibility,Dew_point_temperature,Solar_Radiation,Rainfall,Snowfall,month,weekdays_weekend]]))
    result = (model.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature,Humidity,Wind_speed,Visibility,Dew_point_temperature,Solar_Radiation,Rainfall,Snowfall,month,weekdays_weekend]]))
    return "bike count is {}".format(result)
    #return "bike count is {}".format(Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature,Humidity,Wind_speed,Visibility,Dew_point_temperature,Solar_Radiation,Rainfall,Snowfall,month,weekdays_weekend)



if __name__ == '__main__':
    app.run(debug=True)