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
    
    @classmethod
    def format_data(cls,func):
        pass
        """if output_format=='json':
            data = data.json()
        elif output_format=='pandas':
            print(type(data.content.decode('UTF-8')))
            data = pd.read_csv(io.StringIO(data.content.decode('UTF-8')))
        else:
            raise FMP.FMPException("FMP.format_data: output must be one of pandas or json")"""
