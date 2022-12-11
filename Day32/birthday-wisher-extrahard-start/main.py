##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


# Step 1:
# see birthdays.csv

# Step 2
#
import pandas as pd
import datetime as dt
import random
import smtplib

birthdays = pd.read_csv("birthdays.csv")

birthday_dict = birthdays.to_dict(orient="records")
birthdays_dict = {(datarow["month"], datarow["day"]): datarow for (index, datarow) in birthdays.iterrows()}


now = dt.datetime.now()
print(now)
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for birthday in birthday_dict:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        print("birthday detected!")
        letter = random.choice(letters)
        with open("letter_templates/"+letter) as file:
            letter_text = file.readlines()
            letter_string = ""
            for line in letter_text:
                letter_string += (line)
            letter_string = letter_string.replace("[NAME]", birthday["name"])

            print(letter_string)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("testmaill1289@gmail.com", "tmhodxdyrscsputn")
            connection.sendmail(
                from_addr="testmaill1289@gmail.com",
                to_addrs="testmaill1289@gmail.com",
                msg=f"Subject:Happy Birthday!\n\n{letter_string}"
            )
            print("Did this succeed?")




print("ran out of birthdays to check")





