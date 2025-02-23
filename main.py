import requests
# responses codes we can get from an API https://www.webfx.com/web-development/glossary/http-status-codes/
# latitude and longitude location https://www.latlong.net/Show-Latitude-Longitude.html
# Documentation about APIS errors and requests https://www.notion.so/Codes-you-can-encounter-when-working-with-APIS-1a302ff56c0f80bca561da80c7b8cb85

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
#if response.status_code == 404:
    #raise Exception("That resource doesn't exist")
#if response.status_code == 401:
    #raise Exception("unauthorized")
response.raise_for_status() #very powerful to show exceptions to the user when something fails

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)