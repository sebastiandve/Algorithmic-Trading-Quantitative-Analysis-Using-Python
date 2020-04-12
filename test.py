import pandas_datareader as pdr
import datetime as dt

ticker='AMZN'

end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=365)

df = pdr.get_data_yahoo(ticker, start_date,end_date)
