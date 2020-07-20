import os
import unittest
from unittest.mock import patch
import requests_mock

from fmp_python.fmp import FMP
from fmp_python.common.constants import BASE_URL


@patch.dict(os.environ,{'FMP_API_KEY':'demo'})
class TestFMP(unittest.TestCase):
    @staticmethod
    def get_file_from_name(name):
        script_path = os.path.abspath(__file__)
        script_directory = os.path.dirname(script_path)
        return os.path.join(script_directory,str('test_data'),name)



    @requests_mock.Mocker()
    def test_short_quote(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_quote_short')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/quote-short/AAPL?apikey=demo", text=f.read())
            quote_short = fmp.get_quote_short('AAPL')
            self.assertIsInstance(quote_short,list)

    @requests_mock.Mocker()
    def test_get_quote(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_quote')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/quote/JMCRX,JSMTX,JUESX?apikey=demo", text=f.read())
            quote = fmp.get_quote('JMCRX,JSMTX,JUESX')
            self.assertIsInstance(quote,list)
    
    @requests_mock.Mocker()
    def test_get_quote_index(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_quote_index')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/quote/%5EGSPC?apikey=demo", text=f.read())
            quote = fmp.get_index_quote('GSPC')
            self.assertIsInstance(quote,list)
    
    @requests_mock.Mocker()
    def test_get_historical_chart(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_historical_chart')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/historical-chart/1min/JMCRX?apikey=demo", text=f.read())
            quote = fmp.get_historical_chart('1min','JMCRX')
            self.assertIsInstance(quote,list)

    @requests_mock.Mocker()
    def test_get_historical_chart_index(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_historical_chart_index')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/historical-chart/4hour/%5EGSPC?apikey=demo", text=f.read())
            quote = fmp.get_historical_chart_index('4hour','GSPC')
            self.assertIsInstance(quote,list)

    @requests_mock.Mocker()
    def test_get_historical_price(self, mock_request):
        fmp = FMP()
        file_path = self.get_file_from_name('mock_historical_price')
        with open(file_path) as f:
            mock_request.get(BASE_URL+"/historical-price-full/JMCRX?apikey=demo", text=f.read())
            quote = fmp.get_historical_price('JMCRX')
            self.assertIsInstance(quote,list)
