from enum import Enum
from typing import List

import os
from datetime import datetime

import requests

from fmp_python.common.constants import INDEX_PREFIX
from fmp_python.common.fmpdecorator import FMPDecorator
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

    @FMPDecorator.write_to_file
    @FMPDecorator.format_data
    def get_stock_screener(self, market_cap_lt: int = None, market_cap_gt: int = None, price_lt: int = None,
                           price_gt: int = None, beta_lt: float = None, beta_gt: float = None, volume_lt: int = None,
                           volume_gt: int = None, dividend_lt: float = None, dividend_gt: float = None,
                           is_etf: bool = None, exchange: List[str] = None, sector: List[str] = None,
                           industry: List[str] = None, country: List[str] = ['US'], is_actively_trading: bool = True,
                           limit: int = 1000):
        rb = RequestBuilder(self.api_key)
        rb.set_category('stock-screener')

        rb.set_query_params({'marketCapLowerThan': market_cap_lt, 'marketCapMoreThan': market_cap_gt,
                             'priceLowerThan': price_lt, 'priceMoreThan': price_gt, 'betaLowerThan': beta_lt,
                             'betaMoreThan': beta_gt, 'volumeLowerThan': volume_lt, 'volumeMoreThan': volume_gt,
                             'dividendLowerThan': dividend_lt, 'dividendMoreThan': dividend_gt, 'isEtf': is_etf,
                             'exchange': ','.join(exchange) if exchange is not None else None,
                             'sector': ','.join(sector) if sector is not None else None,
                             'industry': ','.join(industry) if industry is not None else None,
                             'country': ','.join(country) if country is not None else None,
                             'isActivelyTrading': is_actively_trading, 'limit': limit})
        hp = self.__do_request__(rb.compile_request())
        return hp

    @staticmethod
    def __do_request__(url):
        return requests.get(url)
