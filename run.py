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

# local app files
import binance_api


with open(".credentials.yaml", 'r') as credentials_yaml_file:
    credentials_dict = yaml.load(credentials_yaml_file)

    key_api_public_binance = credentials_dict['exchanges']['binance']['public']
    key_api_secret_binance = credentials_dict['exchanges']['binance']['secret']


# result = binance_api.get_pair_trade_history('binance', key_api_public_binance, key_api_secret_binance, 'XVG', 'BTC')

# result = binance_api.get_exchange_balances('binance', key_api_public_binance, key_api_secret_binance)

# print(result)
