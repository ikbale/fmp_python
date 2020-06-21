import os
import functools
import pandas

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
                return response.json()
            elif self.output_format=='pandas':
                pass # TODO format pandas
            else:
                raise Exception("FMP.format_data: output must be one of pandas or json") # TODO manage specific exception

        return _call_wrapper

