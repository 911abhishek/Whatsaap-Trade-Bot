import os
import requests
import json
from bs4 import BeautifulSoup
import time 
apiKey = os.environ.get("market_key")
s = 'P2J3QR2V544JU692'
# BaseUrl = 
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={s}'0
# print(url)

# r = requests.get(url)
# print(r)
# data = r.json()
# print(data)
nse = "https://www.google.com/finance/quote/INFY:NSE"
bom = "https://www.google.com/finance/quote/500209:BOM"


def stockPrice(ticker = "500209",exchange = "Bom"):
    # ticker = "500209"
    # exchange = "Bom"
    url = f"https://www.google.com/finance/quote/{ticker}:NSE"

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    class1 = "YMlKec fxKbKc"
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",",'')) 
    return(price)
def main():
    ticker = str(input())
    # exchange = str(input())
    # y = str("Bom")
    s = stockPrice(ticker)
    print(s)

if __name__ == "__main__":
    main()