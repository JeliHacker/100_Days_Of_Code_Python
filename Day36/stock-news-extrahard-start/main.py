import requests
import config
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_ADVANTAGE_KEY = config.ALPHA_VANTAGE_API_KEY
NEWS_API_KEY = config.NEWSAPI_KEY

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHA_ADVANTAGE_KEY}'
r = requests.get(url)
data = r.json()

most_recent_close_date = list(data["Time Series (Daily)"].keys())[0]
second_most_recent_close_date = list(data["Time Series (Daily)"].keys())[1]

today_data = data["Time Series (Daily)"][most_recent_close_date]
yesterday_data = data["Time Series (Daily)"][second_most_recent_close_date]

close = float(today_data["4. close"])
yesterday_close = float(yesterday_data["4. close"])

percentage_change = abs(((close - yesterday_close) / yesterday_close) * 100)
print(close)
print(yesterday_close)
print(percentage_change)

if percentage_change >= 5:
    print("Get news")
else:
    print("Not a newsworthy close")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
url = (f'https://newsapi.org/v2/everything?'
       f'q={COMPANY_NAME}&'
       'from=2023-01-08&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')

response = requests.get(url)

data = response.json()
most_recent_articles = data['articles'][:3]
print(most_recent_articles)
titles_and_descriptions = [{"title": article["title"], "description": article["description"]} for article in most_recent_articles]
print(titles_and_descriptions)
print(len(titles_and_descriptions))

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

# print(os.environ.keys())
# print(os.path.abspath('.env'))
# print(os.environ.get('TWILIO_ACCOUNT_SID'))

# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN

print(auth_token)
client = Client(account_sid, auth_token)

for article in titles_and_descriptions:
    message_body = article["title"] + "\n" + article["description"]
    message = client.messages.create(
                                  body=message_body,
                                  from_='+13149364762',
                                  to=config.MY_PHONE_NUMBER
                              )

    print(message)
    print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

