from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    message_body = "Low price alert! Only __ to fly from __ to __, from 2020-08-25 to 2020-09-10."

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    def alert_deal(self, price, city1, city2, date1):
        print("There's been a good deal detected!")

        message_body = f"Low price alert! Only ${price} to fly from {city1} to {city2}. The flight leaves on {date1}."

        message = self.client.messages.create(
            body=message_body,
            from_='+13149364762',
            to=os.environ.get('MY_PHONE_NUMBER')
        )

        print(message)
        print(message.status)
