import pandas as pd
import json


# f2c : converts fahrenheit to celcius
# parameters:
#    fahrenheit: the fahrenheit to be converted
#    roundes: true if the result needs to be converted
def f2c(fahrenheit,roundres=True):
    celsius = (fahrenheit - 32) * 5.0/9.0
    celsius = round(celsius,0) if roundres else celsius
    return celsius


# m2k : converts miles to kilometers
# parameters:
#    miles: the miles to be converted
#    roundes: true if the result needs to be converted
def m2k(miles,roundres=True):
    kilometers = float(miles) / 0.62137119
    kilometers = round(kilometers,0) if roundres else kilometers
    return kilometers



forecast_df, = pd.read_html("https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS", header=None, encoding="utf-8")
forecast_df = forecast_df.iloc[:, 1:]
forecast_df.columns = ['TIME', 'DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']

forecast_df['TIME'] =  forecast_df['TIME'].map(lambda x: x[:-3].rstrip().upper() )


for col in ['TEMP', 'FEEL']:
    forecast_df[col] = forecast_df[col].map(lambda x: f2c(int(x[:-1])))

forecast_df['WIND'] = forecast_df['WIND'].map(lambda  x: x.split()[0] +" "+ str(m2k(x.split()[1])) + " km/h")
# for col in ['PRECIP', 'HUMIDITY']:
#     forecast_df[col] = forecast_df[col].map(lambda x: int(x[:-1]))


# calls_df['Time'] = pd.to_datetime(calls_df['Time'])
forecast_df.index=(forecast_df['TIME'])
forecast_df = forecast_df[[ 'DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']]
forecast = json.loads(forecast_df.to_json(orient="index", date_format="iso"))

with open('forcast_data.json','w') as json_fl:
    json.dump(forecast,json_fl, indent=4, sort_keys=True)







