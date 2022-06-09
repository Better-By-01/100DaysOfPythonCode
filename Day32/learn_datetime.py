import datetime as dt

# FOR CURR DATE TIME

now = dt.datetime.now()
# print(now)
# print(type(now))

year = now.year
# print(type(year))


# TO CREATE OWN DATE & TIME
date_of_birth = dt.datetime(year=2002, month=6, day=30)
print(date_of_birth)