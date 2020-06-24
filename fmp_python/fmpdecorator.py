import os
import functools
import pandas as pd
from fmp_python.common.fmpexception import FMPException


class FMPDecorator():

    @classmethod
    def inject_api_key(cls,func):
        @functools.wraps(func)
        def deco_function(*args, **kwargs):
            api_key = os.getenv('FMP_API_KEY')
            request = func(*args, **kwargs)
            if '?' not in request:
                return request+'?apikey='+api_key
            else:
                return request+'&apikey='+api_key
        return deco_function
    
    @classmethod
    def format_data(cls,func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            if self.output_format=='json':
                print(response)
                return response.json()
            elif self.output_format=='pandas':
                return pd.DataFrame(response.json())
            else:
                raise FMPException("Output must be either pandas or json",FMPDecorator.format_data.__name__) 

        return _call_wrapper

