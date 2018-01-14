# utilities
import sys
import requests, urllib
import json, yaml
import time
from datetime import datetime
# cryptography
import hmac, hashlib
# display
import matplotlib.pyplot as mplpyplot
# analysis
import numpy
import pandas
# import keras


def sign_binance(key_api_secret, querystring):
    signature = hmac.new(
        key_api_secret.encode('utf-8'),
        querystring.encode('utf-8'),
        hashlib.sha256,
    ).hexdigest()

    return signature


def get_exchange_balances(exchange, key_api_secret):
    signature = sign_binance(key_api_public, key_api_secret, querystring)

    return


def get_pair_trade_history(exchange, key_api_public, key_api_secret, coin_base, coin_quote):
    if exchange == 'binance':
        url = 'https://api.binance.com/api/v3/myTrades'

        headers = {'X-MBX-APIKEY' : key_api_public}

        timestamp = int(time.time()*1000)
        payload = {
            'timestamp':timestamp,
            'symbol': coin_base + coin_quote,
            # 'fromId': 1, <- binance entry id
        }
        querystring = urllib.parse.urlencode(payload)
        signature = sign_binance(key_api_secret, querystring)

        payload['signature'] = signature
        r = requests.get(url, headers=headers, params=payload)
        j = json.loads(r.text)

        # add human readable field for time for the version passed for display.
        j_pandas = j
        for i, trade in enumerate(j):
            j_pandas[i]['time_utc'] = datetime.fromtimestamp(int(trade['time']/1000))

        df = pandas.DataFrame.from_dict(j_pandas)
        return df
