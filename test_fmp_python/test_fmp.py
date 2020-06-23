import unittest
import os
from unittest.mock import patch
import requests_mock
from fmp_python.fmp import FMP


@patch.dict(os.environ,{'FMP_API_KEY':'demo'})
class TestFMP(unittest.TestCase):
    
    @requests_mock.Mocker()
    def test_short_quote(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_quote_short.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo", text=f.read())
            quote_short = fmp.get_quote_short('AAPL')
            self.assertIsInstance(quote_short,list)

    @requests_mock.Mocker()
    def test_get_quote(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_quote.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/quote/JMCRX,JSMTX,JUESX?apikey=demo", text=f.read())
            quote = fmp.get_quote('JMCRX,JSMTX,JUESX')
            self.assertIsInstance(quote,list)
    
    @requests_mock.Mocker()
    def test_get_quote_index(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_quote_index.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/quote/%5EGSPC?apikey=demo", text=f.read())
            quote = fmp.get_index_quote('GSPC')
            self.assertIsInstance(quote,list)
    
    @requests_mock.Mocker()
    def test_get_historical_chart(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_historical_chart.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/historical-chart/1min/JMCRX?apikey=demo", text=f.read())
            quote = fmp.get_historical_chart('1min','JMCRX')
            self.assertIsInstance(quote,list)

    @requests_mock.Mocker()
    def test_get_historical_chart_index(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_historical_chart_index.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/historical-chart/4hour/%5EGSPC?apikey=demo", text=f.read())
            quote = fmp.get_historical_chart_index('4hour','GSPC')
            self.assertIsInstance(quote,list)

    @requests_mock.Mocker()
    def test_get_historical_price(self, mock_request):
        fmp = FMP()
        file_path = 'D:\\TS_text_mining\\fmp_python\\test_fmp_python\\test_data\\mock_historical_price.txt'#@TODO: function to manage test_data URL
        with open(file_path) as f:
            mock_request.get("https://financialmodelingprep.com/api/v3/historical-price-full/JMCRX?apikey=demo", text=f.read())
            quote = fmp.get_historical_price('JMCRX')
            self.assertIsInstance(quote,list)

 
  