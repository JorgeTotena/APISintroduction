import requests
from send_sms import *
api_key = "a52d9ce51c5eed0cf16d9ccfa0367800"
MY_LAT = 4.395820
MY_LON = -76.069832
UNITS = "metric"
#ACCOUNT_SID =
#AUTH_TOKEN =
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 8,
    "units": UNITS
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print("Status code", response.status_code)
response.raise_for_status()
data = response.json()

#print(data)
#iterating over the JSON file, congratz you were able to do it yourself
list = data["list"][0:8]
Rain = False
for i in list:
    time = i["dt_txt"]
    id = i["weather"][0]["id"]
    description = i["weather"][0]["description"]
    print(time)
    if int(id) <= 700:
        Rain = True
        print("Bring an umbrella")
    print(description)
if Rain:
    message = client.messages.create(
        body="Hay pronóstico de lluvia para las próximas 24 horas.",
        from_="+16612470305",
        to="+573188625128",
    )

    print(message.body)

#print(data["list"][0]["weather"][0]["id"])