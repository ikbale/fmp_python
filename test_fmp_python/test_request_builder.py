import unittest
import os
from unittest.mock import patch
from fmp_python.common.requestbuilder import RequestBuilder

class TestRequestBuilder(unittest.TestCase):
    
    @patch.dict(os.environ,{'FMP_API_KEY':'demo'})
    def test_compile_resquest_category(self):
        rb = RequestBuilder()
        rb.set_category('quote')
        self.assertEqual(rb.compile_request(), "https://financialmodelingprep.com/api/v3/quote?apikey=demo") 
    
    @patch.dict(os.environ,{'FMP_API_KEY':'demo'})
    def test_compile_request_subcategory(self):
        rb = RequestBuilder()
        rb.set_category('quote')
        rb.add_sub_category('^DJI,^GSPC')
        self.assertEqual(rb.compile_request(), "https://financialmodelingprep.com/api/v3/quote/^DJI,^GSPC?apikey=demo")
    
    @patch.dict(os.environ,{'FMP_API_KEY':'demo'})
    def test_compile_request_subcategories(self):
        rb = RequestBuilder()
        rb.set_category('historical-chart')
        rb.add_sub_category('1hour')
        rb.add_sub_category('^GSPC')
        self.assertEqual(rb.compile_request(), "https://financialmodelingprep.com/api/v3/historical-chart/1hour/^GSPC?apikey=demo")

    @patch.dict(os.environ,{'FMP_API_KEY':'demo'})
    def test_compile_resquest_param(self):
        rb = RequestBuilder()
        rb.set_category('balance-sheet-statement')
        rb.add_sub_category('AAPL')
        rb.set_query_params({'period':'quarter'})
        self.assertEqual(rb.compile_request(), "https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?period=quarter&apikey=demo") 