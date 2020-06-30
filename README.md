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
# Method Reference
- Defaut values are output_format = **'json'** and write_to_file = **False** 
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
fmp.get_historical_chart_index('GSPC')
```