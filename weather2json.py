import json

import pandas as pd


# f2c : converts fahrenheit to celsius
# parameters:
#    fahrenheit: the fahrenheit to be converted
#    roundres: true if the result needs to be rounded
def f2c(fahrenheit, roundres=True):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    celsius = round(celsius) if roundres else celsius
    return celsius


# m2k : converts miles to kilometers
# parameters:
#    miles: the miles to be converted
#    roundres: true if the result needs to be rounded
def m2k(miles, roundres=True):
    kilometers = float(miles) / 0.62137119
    kilometers = round(kilometers) if roundres else kilometers
    return kilometers


# weather2json : reads the weather forecast from weather.com
# parameters:
#    output_file: The file where the JSON will be saved.
def weather2json(output_file):
    forecast_df, = pd.read_html("https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS", header=None, encoding="utf-8")
    forecast_df = forecast_df.iloc[:, 1:]
    forecast_df.columns = ['TIME', 'DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']

    # The output of the time comes in format of '12:00 pm Tue' or '12:00 amWed' .
    # Below we are removing the 3 letters of the day.
    forecast_df['TIME'] = forecast_df['TIME'].map(lambda x: x[:-3].rstrip().upper())

    # The temperature values comes in fahrenheit which we convert below to celsius
    for col in ['TEMP', 'FEEL']:
        forecast_df[col] = forecast_df[col].map(lambda x: f2c(int(x[:-1])))

    forecast_df['WIND'] = forecast_df['WIND'].map(lambda x: x.split()[0] + " " + str(m2k(x.split()[1])) + " km/h")
    forecast_df.index = (forecast_df['TIME'])
    forecast_df = forecast_df[['DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']]

    # We could have just put the result of forecast_df.to_json to the output file but in order to format the
    # Output we need to go trough the json type.
    forecast = json.loads(forecast_df.to_json(orient="index", date_format="iso"))

    with open(output_file, 'w') as json_fl:
        json.dump(forecast, json_fl, indent=4, sort_keys=True)


if __name__ == "__main__":
    weather2json('forcast_data.json')

# EOF
