# code can't be tested as email account is secured and option to lower its security is no more available

import smtplib

my_email = "singhpatelashutosh@yahoo.com"
password = "kiihidfyabvqdpda"

connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
connection.starttls()                                       # way of securing our connection to the email server
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="2005017@kiit.ac.in", 
    msg="Subject:Hello\n\nThis is the body of my email")    # if subject not provided then the email will be marked as spam 
connection.close()

# OR using with and not writing connection.close()
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()                                       # way of securing our connection to the email server
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="patelsinghashutosh@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email")    # if subject not provided then the email will be marked as spam 
