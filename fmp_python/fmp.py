import pandas as pd
import requests
import os
import io

class FMP(object):
    """
    Base class that implements  api calls 
    """
    _API_VERSION = "v3/"
    _FMP_API_BASE_URL = "https://financialmodelingprep.com/api/"+_API_VERSION
    _INDEX_SYMBOL = "^"

    class FMPException(Exception):
        pass

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('FMP_API_KEY')


    def get_quote_short(self, symbol):
        quote = requests.get(FMP._FMP_API_BASE_URL+"/quote-short/"+symbol+"?apikey="+self.api_key)
        return quote

    def get_index_quote(self,symbol):
        index_quote = requests.get(FMP._FMP_API_BASE_URL+"/quote/"+FMP._INDEX_SYMBOL+symbol+"?apikey="+self.api_key)
        return index_quote

    def format_data(self, data, output_format='pandas'):
        if output_format=='json':
            data = data.json()
        elif output_format=='pandas':
            data = pd.read_csv(io.StringIO(data.content.decode('UTF-8')))
        else:
            raise FMP.FMPException("FMP.format_data: output must be one of pandas or json")



def main():
    fmp = FMP()
    indexes = fmp.get_quote_short('AAL')
    fmp.format_data(indexes)

if __name__ == "__main__":
    main()