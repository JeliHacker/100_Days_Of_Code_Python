import smtplib
import datetime as dt
import random

MY_EMAIL = "testmaill1289@gmail.com"
MY_PASSWORD = "tmhodxdyrscsputn"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


