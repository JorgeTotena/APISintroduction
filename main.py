from datetime import datetime
import requests
import smtplib
MY_EMAIL = "tj0695646@gmail.com"
MY_PASSWORD = "12345678Ab"
MY_LAT = 4.570868
MY_LNG = -74.297333
# responses codes we can get from an API https://www.webfx.com/web-development/glossary/http-status-codes/
# latitude and longitude location https://www.latlong.net/Show-Latitude-Longitude.html
# Documentation about APIS errors and requests https://www.notion.so/Codes-you-can-encounter-when-working-with-APIS-1a302ff56c0f80bca561da80c7b8cb85


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    #if response.status_code == 404:
        #raise Exception("That resource doesn't exist")
    #if response.status_code == 401:
        #raise Exception("unauthorized")
    response.raise_for_status() #very powerful to show exceptions to the user when something fails

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(iss_position)

    #Your position is within +5 or -5 degrees of your position

    if MY_LAT -5 <= latitude <= MY_LAT + 5 >= latitude and MY_LNG -5 <= longitude <= MY_LNG -5:
        return True

def is_night():
    #APIS with parameters

    paramaters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    reponse = requests.get("https://api.sunrise-sunset.org/json", params=paramaters)
    reponse.raise_for_status()
    data = reponse.json()
    #sunrise = data["results"]["sunrise"]
    #sunset = data["results"]["sunset"]
    timenow = datetime.now().hour
    #print(sunset)
    sunrise_hour  = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    if timenow >= sunset_hour and timenow <= sunrise_hour:
        return True
    #print(data)

connection = smtplib.SMTP("smtp.@gmail.com", 587)
connection.starttls()
connection.login(MY_EMAIL, MY_PASSWORD)
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg="Subject:Look Up \n\n The ISS is above your head in the sky"
)

"""while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp@gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up \n\n The ISS is above your head in the sky"
        ) """


