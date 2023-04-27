# Raw Package
import numpy as np 
import pandas as pd
from pandas_datareader import data as pdr 

# Market Data 
import yfinance as yf

# Graphing / Visualization 
import plotly.graph_objs as go

# Connect to the Yahoo Finance stock API 
yf.pdr_override()

# Specify the stock you want to get data for
stock=input("Enter a stock symbol: ")
print(stock)

'''
ticker: case insensitive ticker of the desired stock/bond
start_date: date you want the data to start from (mm/dd/yyyy)
end_date: date you want the data to end (mm/dd/yyyy)
index_as_date: {True, False}. Default is true. If true then the dates of the records are set as the index, else they are returned as a separate column.
interval: {“1d”, “1wk”, “1mo”}. Refers to the interval to sample the data: “1d”= daily, “1wk”= weekly, “1mo”=monthly.
'''

# Import the data frame (df) from yahoo finance using the specified stock as the ticker symbol
df = yf.download(tickers=stock,period='1d',interval='1m')

# Print the data we have requested
print(df)


# Visualize the data 
fig=go.Figure()

fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'], name = 'market data'))

fig.update_layout(
    title= str(stock)+' Live Share Price:',
    yaxis_title='Stock Price (USD per Shares)')               

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.show()