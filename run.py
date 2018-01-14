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

    key_api_binance_public = credentials_dict['exchanges']['binance']['public']
    key_api_binance_secret = credentials_dict['exchanges']['binance']['secret']


text = binance_api.get_trade_history('binance', key_api_binance_public, key_api_binance_secret, 'LTC', 'BTC')
print(text)
