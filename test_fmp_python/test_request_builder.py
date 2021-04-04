import unittest
import os
from unittest.mock import patch
from fmp_python.common.constants import BASE_URL
from fmp_python.common.requestbuilder import RequestBuilder

@patch.dict(os.environ,{'FMP_API_KEY':'demo'})
class TestRequestBuilder(unittest.TestCase):
    
    def test_compile_resquest_category(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('quote')
        self.assertEqual(rb.compile_request(), BASE_URL+"/quote?apikey=demo") 
    
    def test_compile_request_subcategory(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('quote')
        rb.add_sub_category('^DJI,^GSPC')
        self.assertEqual(rb.compile_request(), BASE_URL+"/quote/^DJI,^GSPC?apikey=demo")
    
    def test_compile_request_subcategories(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('historical-chart')
        rb.add_sub_category('1hour')
        rb.add_sub_category('^GSPC')
        self.assertEqual(rb.compile_request(), BASE_URL+"/historical-chart/1hour/^GSPC?apikey=demo")

    def test_compile_resquest_param(self):
        rb = RequestBuilder(api_key='demo')
        rb.set_category('balance-sheet-statement')
        rb.add_sub_category('AAPL')
        rb.set_query_params({'period':'quarter'})
        self.assertEqual(rb.compile_request(), BASE_URL+"/balance-sheet-statement/AAPL?period=quarter&apikey=demo")
         