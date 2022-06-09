import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "singhpatelashutosh@yahoo.com"
PASSWORD = "kiihidfyabvqdpda"


curr_date = dt.datetime.now()
today_tuple = (curr_date.month, curr_date.day)

# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv("/home/giba/100DaysOfPythonCode/Day32/automated_bday_wisher/birthdays.csv")
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# key is going to be the tuple consisting of (birthday_month, birthday_day)

birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in df.iterrows()} 
# format we want
# birthdays_dict = {
#   (12,24): Angela, angela@email.com,1995,12,24 
# }

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    FILE_PATH=f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(FILE_PATH) as letter_file:
        contents = letter_file.read()                           #strings
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




