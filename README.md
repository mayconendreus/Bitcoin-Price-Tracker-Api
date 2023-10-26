# Bitcoin-Price-Tracker-Api
Here is a  code for a Bitcoin Tracker that notify me by email the price of Bitcoin every 60 seconds 

The provided code is a Python script that continuously tracks the price of Bitcoin and sends an email notification with the current price every minute using data from AlphaVantage. Here's a breakdown of the code:

Import necessary libraries:

import requests: This library is used for making HTTP requests to the AlphaVantage API to fetch cryptocurrency price data.
import time: This library is used to introduce a delay of one minute between price checks.
import smtplib: This library is used to send email notifications.
import ssl: SSL is used to establish a secure connection for sending email notifications.
Define the send_email function:

This function is responsible for sending email notifications.
It sets up the SMTP server and login credentials, including sender and receiver email addresses.
The email server is configured for Gmail, and you should replace the placeholder values (email_from and pswd) with your actual email and password.
The function uses SSL for a secure email connection.
If the email is sent successfully, a confirmation message is printed; otherwise, an error message is printed.
Set the AlphaVantage API key, symbol, and run the tracking loop:

api_key: This variable stores your AlphaVantage API key, which is used to access cryptocurrency price data.
symbol: This variable stores the symbol for the cryptocurrency you want to track, which is set to "BTC" for Bitcoin.
The code enters an infinite loop (while True) to continuously monitor the price.
Inside the loop:

The script constructs the URL to fetch the real-time exchange rate data for Bitcoin to USD using the AlphaVantage API.
It makes an HTTP GET request to the URL and stores the response in the data variable after converting it to JSON format.
Check if the response contains the required data:

The script checks if the response contains the key "Realtime Currency Exchange Rate" to ensure it has received the expected data.
If the data is present, the script extracts the current price of Bitcoin in USD from the response and prints it.
Send an email notification:

The send_email function is called with the Bitcoin symbol and the current price as arguments to send an email with the price information.
Handle errors:

If there are any issues with the API request or email sending, error messages are printed, but the script continues running.
Wait for one minute:

After each iteration of the loop, the script sleeps for one minute (60 seconds) using time.sleep(60) to ensure that the price is checked every minute.
You should replace the placeholder values with your actual email credentials, and you can customize the code further to track different cryptocurrencies or adjust the timing of price checks. Make sure to use a secure method to store your email credentials, such as environment variables or a configuration file, to keep them safe.
