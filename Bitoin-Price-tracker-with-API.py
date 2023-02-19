


# Bitcoin price tracker 
# That notify me avery minute sending mew a email 
# Using Api Key from AlphaVantage

import requests
import time
import smtplib
import ssl

def send_email(price):
    smtp_port = 587
    smtp_server = "smtp.gmail.com" # server email
    email_from = "###################" # sender email used to sent the email notification price 
    email_to = "##################" # receiver email 
    pswd = ################## Here goes the password that google ill generate for you 
    

    simple_email_context = ssl.create_default_context()

    try:
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        TIE_server.sendmail(email_from, email_to,price ) 

        print("Email sent successfully!")
        #This txt ill print if my email its has been sent 
    except Exception as e:
        print("Error sending email:", e)
        # This error message ill pop if is something wrong 
    finally:
        TIE_server.quit()

api_key = "####################" # Here we got a api key from the website AlphaVantage to connect to the data 
symbol = "BTC" # Bitcoin symbol 

while True:
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency=USD&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "Realtime Currency Exchange Rate" in data:
        price = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        print(f"Current price of {symbol}: {price}")
        send_email( symbol  +   price ) #Txt ill be printed with the symbol BTC and currently price of BITCOIN
         
    else:
        print(f"Failed to extract price for {symbol}")

    time.sleep(60) # i set up 60 seconds one minute but it can be configured as user prefer 
