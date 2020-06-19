import os
import functools
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
        