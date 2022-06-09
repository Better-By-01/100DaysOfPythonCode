import datetime as dt
import smtplib
import random

MY_EMAIL = "singhpatelashutosh@gmail.com"
PASSWORD = "ap317151@gmail.com" 

with open("/home/giba/100DaysOfPythonCode/Day32/challenge1/quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)

curr_date = dt.datetime.now()

if curr_date.weekday == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:        # 587 for TLS & 465 for SSL
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
