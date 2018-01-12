import requests
import json

def get_trade_history():
    url = 'http://google.com'
    resp = requests.get(url)

    return resp.text


text = get_trade_history()
print(text)
