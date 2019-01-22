# verint-home-assignment

* [Assginment description][#sssginment-description]
    * [Step 1][#step-1-python-or-bash]
    * [Step 2][#step-2]
    * [Guidelines][#guidelines]
* [Prerequisites][#prerequisites]
* [Jenkins Pipeline][jenkins-pipeline]

## Assginment description 

### Step 1 (Python or Bash):
Write a python script named "forcast_collector" that will collect the hourly temperature from
the following site:  
https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS  
And save the table data in a json file named "forcast_data.json.  
Json Structure:
```JSON
{
    "time": {
        "DESC": "Rain|Showers",
        "TEMP": "Temperature",
        "FEEL": "Temperature",
        " PRECIP": "% precip",
        "HUMIDITY": "% humidity",
        "WIND" : "Wind description"
    }
}
```
Example:

```JSON
{
    "12:00 AM": {
        "DESC": "Rain ",
        "TEMP": "14",
        "FEEL": "12",
        " PRECIP": "70%",
        "HUMIDITY": "90% ",
        "WIND" : "SSE 8 km/h"
    }
}
```

### Step 2:
Create MD5Sum file for the script  

Upload the script & the MD5 into Github.  

Write Jenkins pipeline job with Jenkinsfile that will perform the following:
- Checkout the Github repository.
- Stage 1: Verify the MD5 against the script file.
- Stage 2: execute the script.
- Stage 3: Validate "temperature_data.json" structure (make sure the json structure is
OK).

### Guidelines:
- The script should work on ubuntu servers.
- Write clean code
- Comments are welcome.
- In case a special package is required add a comment with the following information:
o Name of the package.
o What the package does.
o Which command was used to install the package?
Adding pip requirements file will be nice
- Once the code is ready send us a link to the GitHub repository.

## Prerequisites
The following packages needs to be installed:
```
pandas
```

OR you can use the requirements.txt file instead 
```bash
pip install -r requirements.txt
```

The pandas package is a powerful Python data analysis toolkit. In our script we use it to extract data from the forecast website in a tabular format.

## Jenkins Pipeline
In this repo there is  a `Jenkinsfile` which can be used into a jenkins server in order to fulfill [Step 2][#step-2]

In adition to what was required in step 2 the pipeline also use the hash.md5 file to validate the `requirements.txt` 
 