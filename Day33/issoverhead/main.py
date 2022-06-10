import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351                               # London
MY_LONG = -0.127758 

MY_EMAIL = "singhpatelashutosh@yahoo.com"
MY_PASSWORD = "kiihidfyabvqdpda"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if ((MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5)):
        return True




def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)
    time_now = datetime.now()

    if (sunset <= time_now.hour <= sunrise):
        return True

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs="2005017@kiit.ac.in",
                msg="Subject: Look Up ^ \n\n The ISS is above you in the sky."
            )



# BONUS: run the code every 60 seconds.



