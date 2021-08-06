from bs4 import BeautifulSoup
import requests

def bitcoin():
    url = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }

    req_btc = requests.get(url, headers=headers)
    source_btc = req_btc.text

    soup = BeautifulSoup(source_btc, 'lxml')
    total_price = soup.find(class_="arial_26 inlineblock pid-945629-last")

    req_time = req_btc.text
    time_now = soup.find(class_="bold pid-945629-time")

    print('BTC/USD:', total_price.text+'$')
    print('Время обновления:', time_now.text)
    print()

def Etherium():
    url = 'https://ru.investing.com/crypto/ethereum'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }

    req_eth = requests.get(url, headers=headers)
    source_eth = req_eth.text

    soup = BeautifulSoup(source_eth, 'lxml')
    total_price = soup.find(class_="pid-1061443-last")

    req_time = req_eth.text
    time_now = soup.find(class_="bold pid-1061443-time")

    print('ETH/USD:', total_price.text+'$')
    print('Время обновления:', time_now.text)
    print()

def Dash():
    url = 'https://ru.investing.com/crypto/dash'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }

    req_dash = requests.get(url, headers=headers)
    source_eth = req_dash.text

    soup = BeautifulSoup(source_eth, 'lxml')
    total_price = soup.find(class_="pid-1061456-last")

    req_time = req_dash.text
    time_now = soup.find(class_="bold pid-1061456-time")

    print('DASH/USD:', total_price.text+'$')
    print('Время обновления:', time_now.text)
    print()

while True:
    print('Выберите валюту, чтобы узнать её курс:')
    choice = int(input('BTC - 1, ETH - 2, DASH - 3: '))
    waiting = print('Пожалуйста, подождите.Отправляем запрос.')
    if choice == 1:
        bitcoin()
    if choice == 2:
        Etherium()
    if choice == 3:
        Dash()
