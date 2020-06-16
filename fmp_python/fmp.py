import pandas as pd
import requests
import os

class FMP(object):
    _FMP_API_BASE_URL = "https://financialmodelingprep.com/api/v3/"


    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('FMP_API_KEY')


    def get_quote_short(self, symbol, output_format='json'):
        quote = requests.get(FMP._FMP_API_BASE_URL+"/quote-short/"+symbol+"?apikey="+self.api_key)
        if output_format == 'json':
            quote = quote.json()
        return quote


def main():
    fmp = FMP()
    print(fmp.get_quote_short('AAL'))

if __name__ == "__main__":
    main()