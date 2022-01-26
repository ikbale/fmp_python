from enum import Enum

import requests
import os
from datetime import datetime

import requests

from fmp_python.common.constants import INDEX_PREFIX
from fmp_python.common.fmpdecorator import FMPDecorator
from fmp_python.common.fmpexception import FMPException
from fmp_python.common.fmpvalidator import FMPValidator
from fmp_python.common.requestbuilder import RequestBuilder

"""
Base class that implements api calls 
"""


class Interval(Enum):
    MIN_1 = "1min"
    MIN_5 = "5min"
    MIN_15 = "15min"
    MIN_30 = "30min"
    HOUR_1 = "1hour"
    HOUR_4 = "4hour"


class FMP(object):

    def __init__(self, api_key=None, output_format='pandas', write_to_file=False):
        self.api_key = api_key or os.getenv('FMP_API_KEY')
        self.output_format = output_format
        self.write_to_file = write_to_file
        self.current_day = datetime.today().strftime('%Y-%m-%d')

    @FMPDecorator.write_to_file
    @FMPDecorator.format_data
    def get_quote_short(self, symbol):
        rb = RequestBuilder(self.api_key)
        rb.set_category('quote-short')
        rb.add_sub_category(symbol)
        quote = self.__do_request__(rb.compile_request())
        return quote

    @FMPDecorator.write_to_file
    @FMPDecorator.format_data
    def get_quote(self, symbol):
        rb = RequestBuilder(self.api_key)
        rb.set_category('quote')
        rb.add_sub_category(symbol)
        quote = self.__do_request__(rb.compile_request())
        return quote

    def get_index_quote(self, symbol):
        return FMP.get_quote(self, str(INDEX_PREFIX) + symbol)

    @FMPDecorator.write_to_file
    @FMPDecorator.format_data
    def get_historical_chart(self, symbol, interval: Interval):
        rb = RequestBuilder(self.api_key)
        rb.set_category('historical-chart')
        rb.add_sub_category(interval.value)
        rb.add_sub_category(symbol)
        hc = self.__do_request__(rb.compile_request())
        return hc

    def get_historical_chart_index(self, symbol: str, interval: Interval):
        return FMP.get_historical_chart(self, str(INDEX_PREFIX) + symbol, interval)

    @FMPDecorator.write_to_file
    @FMPDecorator.format_historical_data
    def get_historical_price(self, symbol: str, limit: int = None):
        rb = RequestBuilder(self.api_key)
        rb.set_category('historical-price-full')
        rb.add_sub_category(symbol)
        rb.set_query_params({'timeseries': limit})
        hp = self.__do_request__(rb.compile_request())
        return hp

    @staticmethod
    def __do_request__(url):
        return requests.get(url)
