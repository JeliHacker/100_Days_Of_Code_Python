import smtplib

my_email = "testmail125@yahoo.com"
password = "123go123"

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user = my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testmaill1289@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

