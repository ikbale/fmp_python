import os
import sys
import functools
import pandas as pd
from datetime import datetime

from fmp_python.common.fmpexception import FMPException


class FMPDecorator():

    @classmethod
    def inject_api_key(cls, func):
        @functools.wraps(func)
        def deco_function(self, *args, **kwargs):
            api_key = self.api_key
            request = func(self, *args, **kwargs)
            if '?' not in request:
                return request + '?apikey=' + api_key
            else:
                return request + '&apikey=' + api_key
        return deco_function

    @classmethod
    def format_data(cls, func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            if self.output_format == 'json':
                return response.json()
            elif self.output_format == 'pandas':
                return pd.DataFrame(response.json())
            else:
                raise FMPException("Output must be either pandas or json",
                                   FMPDecorator.format_data.__name__)

        return _call_wrapper

    @classmethod
    def format_historical_data(cls, func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            resp = response.json()
            if self.output_format == 'json':
                return resp.get('historical', [])
            elif self.output_format == 'pandas':
                return pd.DataFrame(resp.get('historical', []))
            else:
                raise FMPException("Output must be either pandas or json",
                                   FMPDecorator.format_historical_data.__name__)

        return _call_wrapper

    @classmethod
    def write_to_file(cls, func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            if self.write_to_file:
                category = func.__name__.replace('get_', '')
                symbol = args[len(args) - 1]
                fullname = FMPDecorator.__build_output_tree(symbol, category)
                if self.output_format == 'json':
                    pd.DataFrame(response).to_excel(fullname)
                else:
                    response.to_excel(fullname)
            return response
        return _call_wrapper

    @classmethod
    def __build_output_tree(cls, symbol, category):
        current_day = datetime.today().strftime('%Y-%m-%d')
        current_full_date = datetime.now().strftime("%d-%m-%Y_%Hh%Mmin%Ss")

        filename = '_'.join([symbol, current_full_date])
        _root = '{}'.format('C:' if sys.platform == 'win32' else '/')
        outdir = os.path.join(_root, 'tmp', category, current_day)
        os.makedirs(outdir, exist_ok=True)
        fullname = os.path.join(outdir, filename + '.xlsx')
        return fullname
