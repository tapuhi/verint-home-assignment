import json
import sys

import pandas as pd

FORECAST_URL = "https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS"


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
    try:
        forecast_df, = pd.read_html(FORECAST_URL, header=None, encoding="utf-8")
    except Exception as e:
        print("Failed to gather weather forcase from {forecast_link} - {err}".format(forecast_link=FORECAST_URL,
                                                                                     err=str(e)))
        sys.exit(1)

    forecast_df = forecast_df.iloc[:, 1:]
    forecast_df.columns = ['TIME', 'DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']

    # The output of the time comes in format of '12:00 pm Tue' or '12:00 amWed' .
    # Below we are removing the 3 letters of the day.
    forecast_df['TIME'] = forecast_df['TIME'].map(lambda x: x[:-3].rstrip().upper())

    # The temperature values comes in fahrenheit which we convert below to celsius
    for col in ['TEMP', 'FEEL']:
        forecast_df[col] = forecast_df[col].map(lambda x: f2c(int(x[:-1])))

    # The wind speed comes in Miles per hour which we need to convert to km/h
    forecast_df['WIND'] = forecast_df['WIND'].map(lambda x: x.split()[0] + " " + str(m2k(x.split()[1])) + " km/h")
    forecast_df.index = (forecast_df['TIME'])
    forecast_df = forecast_df[['DESC', 'TEMP', 'FEEL', 'PRECIP', 'HUMIDITY', 'WIND']]

    # We could have just put the result of forecast_df.to_json to the output file but in order to format the
    # Output we need to go trough the json type.
    forecast = json.loads(forecast_df.to_json(orient="index", date_format="iso"))

    try:
        with open(output_file, 'w') as json_fl:
            json.dump(forecast, json_fl, indent=4, sort_keys=True)
    except IOError as e:
        print("I/O error({errno}) while trying to open file {fl}: {errmsg}".format(errno=e.errno,
                                                                                   fl=output_file,
                                                                                   errmsg=e.strerror))
        sys.exit(1)
    except Exception as e:
        print ("Unexpected error while trying to open file {fl}: {err}".format(fl=output_file,
                                                                               err=str(e)))
        sys.exit(1)


if __name__ == "__main__":
    weather2json('forcast_data.json')

# EOF
