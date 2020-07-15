[![Build Status](https://travis-ci.com/ikbale/fmp_python.svg?branch=master)](https://travis-ci.com/ikbale/fmp_python)
[![PyPI version](https://badge.fury.io/py/fmp-python.svg)](https://badge.fury.io/py/fmp-python)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/ikbale/fmp_python.svg)](http://isitmaintained.com/project/ikbale/fmp_python "Average time to resolve an issue")
[![Percentage of issues still open](https://isitmaintained.com/badge/open/ikbale/fmp_python.svg)](http://isitmaintained.com/project/ikbale/fmp_python "Percentage of issues still open")
# Financial Modeling Prep Python Module

Python module to get stock data from the Financial Modeling Prep API

# Install
This library requires you to have an account with Financial Modeling Prep (sign up [here](https://financialmodelingprep.com/))

You can install the package:
- Using **pip**:
```
pip install fmp_python
```
- From the source:
```
git clone https://github.com/ikbale/fmp_python.git

pip install -e fmp_python
```
# Usage
To get data from the API:
- import the library and call the object with your API key:
```
from fmp_python.fmp import FMP

fmp = FMP(api_key='YOUR_API_KEY')
fmp.get_quote('AAL')
```
- Or, you can store it in the environment variable FMP_API_KEY
```
from fmp_python.fmp import FMP

fmp = FMP(output_format='pandas', write_to_file=True)
fmp.get_quote('AAL')
```
You can choose which output format you want your data **output_format = 'pandas' or 'json'**. 

*'json' is the default value*

You can also choose if you want the output to be stored in a file (in C:/tmp) by setting **write_to_file = True**

*'False' is the default value*

## Real Time Stock Price
*Reference*: https://financialmodelingprep.com/developer/docs/#Company-Quote
```
fmp.get_quote(symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.get_quote('AAL')
```
## Stock Time Series
### 1. Stock Price
*Reference*: https://financialmodelingprep.com/developer/docs/#Stock-Price
```
fmp.get_quote_short(symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.quote_short('AAL')
```
### 2. Stock Historical Price
*Reference*: https://financialmodelingprep.com/developer/docs/#Stock-Historical-Price
```
fmp.get_historical_chart(interval:str, symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.get_historical_chart('5min','AAL')
```
## Market Indexes
### 1. Most of the majors indexes (Dow Jones, Nasdaq, S&P 500)
*Reference*: https://financialmodelingprep.com/developer/docs/#Most-of-the-majors-indexes-(Dow-Jones,-Nasdaq,-S&P-500) 
```
fmp.get_index_quote(symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.get_index_quote('GSPC')
```
### 2. Historical stock index prices
*Reference*: https://financialmodelingprep.com/developer/docs/#Historical-stock-index-prices

- By timelapse:
```
fmp.get_historical_chart_index(interval:str,symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.get_historical_chart_index('5min', GSPC')
```
- Daily:
```
fmp.get_historical_price(symbol: str)
```
*Usage Example*
```
fmp = FMP(output_format = 'pandas', write_to_file= True)
fmp.get_historical_price('GSPC')
```