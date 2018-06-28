import configparser
import quandl
import plotly.graph_objs as go 
import plotly.offline as pyo 

parser = configparser.ConfigParser()
parser.read("data/API.ini")
SECRET_KEY = parser.get('API','secret_key')


quandl.ApiConfig.api_key = SECRET_KEY
ltc_usd_data = quandl.get('BITFINEX/LTCUSD', start_date='2017-08-01', end_date='2018-07-30')
btc_usd_data = quandl.get('BITFINEX/BTCUSD', start_date='2017-08-01', end_date='2018-07-30')
print(ltc_usd_data.head(5))


line1 = go.Scatter(x = ltc_usd_data.index,
                   y = ltc_usd_data["Mid"],
                   mode = 'lines',
                   name = 'LTC/USD' )
line2 = go.Scatter(x = btc_usd_data.index,
                   y = btc_usd_data["Mid"]/100,
                   mode = 'lines',
                   name = 'BTC/USD OVER 100' )                  
                                  
              
data = [line1, line2]
layout = go.Layout(title = 'Cryptocurrency Market: LTC/USD vs BTC/USD OVER 100', 
                   xaxis = {'title': 'Time (months)'},
                   yaxis = {'title': 'Price'},
                   hovermode = 'closest')

figure = go.Figure(data = data, layout = layout)

pyo.plot(figure, 
        filename = 'crypto/crypto.html')         
