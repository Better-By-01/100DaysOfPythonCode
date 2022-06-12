from email import message
import requests
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "05YDUIHCNSIZZB7L"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api,
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# USING LIST COMPREHENSION HERE
# data_list = [value for (key, value) in data.items()]

data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

stock_price_diff = yesterday_closing_price - day_before_yesterday_closing_price
inc_dec_per = round(abs(stock_price_diff/yesterday_closing_price)*100, 2)

if (inc_dec_per >= 3):
    print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_api = "c0de1de0262b4cea863f11465488ad16"

news_params = {
    "q": COMPANY_NAME,
    "apiKey": news_api,
    "pageSize": 3,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_articles = news_response.json()["articles"]

symbol = None

if stock_price_diff > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

articles_list = [f"{STOCK}: {symbol}{inc_dec_per}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]
print(articles_list)

account_sid = "AC1ad7901045f9691b7ba6b97cae816fc6"
auth_token = "d81c65cbdf2d68934ae18ca8f8c20599"
client = Client(account_sid, auth_token)

for article in articles_list:
    message = client.messages \
                    .create(
                        body=article,
                        from_='+17164588302',
                        to='+917735927805',
                    )
    print(message.sid)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

