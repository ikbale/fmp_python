import os
import unittest
from unittest.mock import patch

from fmp_python.common.constants import BASE_URL
from fmp_python.common.requestbuilder import RequestBuilder
from fmp_python.fmp import Interval, FMP


@patch.dict(os.environ, {'FMP_API_KEY': 'demo'})
class TestRequestBuilder(unittest.TestCase):

    def test_compile_request_category(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('quote')
        self.assertEqual(rb.compile_request(), BASE_URL + "/quote?apikey=demo")

    def test_compile_request_subcategory(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('quote')
        rb.add_sub_category('^DJI,^GSPC')
        self.assertEqual(rb.compile_request(), BASE_URL + "/quote/^DJI,^GSPC?apikey=demo")

    def test_compile_request_subcategories(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('historical-chart')
        rb.add_sub_category(Interval.HOUR_1.value)
        rb.add_sub_category('^GSPC')
        self.assertEqual(rb.compile_request(), BASE_URL + "/historical-chart/1hour/^GSPC?apikey=demo")

    def test_compile_request_param(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('balance-sheet-statement')
        rb.add_sub_category('AAPL')
        rb.set_query_params({'period': 'quarter'})
        self.assertEqual(rb.compile_request(), BASE_URL + "/balance-sheet-statement/AAPL?period=quarter&apikey=demo")

    def test_compile_stock_screener(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('stock-screener')
        rb.set_query_params({'limit': 2000, 'betaMoreThan': 0.8, 'exchange': ','.join(['NYSE', 'NASDAQ']),
                             'priceMoreThan': 20, 'priceLessThan': 500, 'marketCapMoreThan': 100000000})
        self.assertEqual(rb.compile_request(), BASE_URL +
                         "/stock-screener?marketCapMoreThan=100000000&priceLessThan=500&priceMoreThan=20"
                         "&exchange=NYSE,NASDAQ&betaMoreThan=0.8&limit=2000&apikey=demo")
