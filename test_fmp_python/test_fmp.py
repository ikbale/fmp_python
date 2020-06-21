import unittest
import os
from unittest.mock import patch
from fmp_python.fmp import FMP

@patch.dict(os.environ,{'FMP_API_KEY':'demo'})
class TestFMP(unittest.TestCase):
    
    def test_request_short(self):
        fmp = FMP()
        quote_short = fmp.get_quote_short('AAL') # TODO assert
        self.assertTrue(True) 
  