import os
import functools

class FMPDecorator():

    @classmethod
    def inject_api_key(cls,func):
        api_key = os.getenv('FMP_API_KEY')
        @functools.wraps(func)
        def deco_function(*args, **kwargs):
            request = func(*args, **kwargs)
            if '?' not in request:
                return request+'?apikey='+api_key
            else:
                return request+'&apikey='+api_key
        return deco_function
                      