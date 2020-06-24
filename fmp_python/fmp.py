import pandas as pd
import requests
import os
import io
from fmp_python.constants import BASE_URL
from fmp_python.constants import INDEX_PREFIX
from fmp_python.common.requestbuilder import RequestBuilder
from fmp_python.fmpdecorator import FMPDecorator
from fmp_python.fmpvalidator import FMPValidator
from fmp_python.common.fmpexception import FMPException



class FMP(object):
    """
    Base class that implements  api calls 
    """

    def __init__(self, api_key=None, output_format='json'):
        self.api_key = api_key or os.getenv('FMP_API_KEY')
        self.output_format = output_format


    @FMPDecorator.format_data
    def get_quote_short(self, symbol):
        rb = RequestBuilder()
        rb.set_category('quote-short')
        rb.add_sub_category(symbol)
        quote = requests.get(rb.compile_request())
        return quote
    
    @FMPDecorator.format_data
    def get_quote(self,symbol):
        rb = RequestBuilder()
        rb.set_category('quote')
        rb.add_sub_category(symbol)
        quote = requests.get(rb.compile_request())
        return quote

    def get_index_quote(self,symbol):
        return FMP.get_quote(self,str(INDEX_PREFIX)+symbol)
    
    @FMPDecorator.format_data
    def get_historical_chart(self, interval, symbol):
        if FMPValidator.is_valid_interval(interval):
            rb = RequestBuilder()
            rb.set_category('historical-chart')
            rb.add_sub_category(interval)
            rb.add_sub_category(symbol)
            hc = requests.get(rb.compile_request())
            return hc
        else:
            raise FMPException('Interval value is not valid',FMP.get_historical_chart.__name__)

    def get_historical_chart_index(self,interval,symbol):
        return FMP.get_historical_chart(self, interval, str(INDEX_PREFIX)+symbol)

    @FMPDecorator.format_data
    def get_historical_price(self,symbol):
        rb = RequestBuilder()
        rb.set_category('historical-price-full')
        rb.add_sub_category(symbol)
        hp = requests.get(rb.compile_request())
        return hp




   
