import datetime as dt
import pandas_datareader.data as pdr

result = pdr.get_quote_yahoo('JPY=X')
ary_result = result["price"].values
price = ary_result[0]
print(price)