# import smtplib
#
# my_email = "testmail125@yahoo.com"
# password = "123go123"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user = my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="testmaill1289@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)