# Raw Package
import numpy as np 
import pandas as pd
from pandas_datareader import data as pdr 

# Market Data 
import yfinance as yf

# Graphing / Visualization 
import plotly.graph_objs as go

# Web App Framework
from flask import Flask, render_template

# Specify the stock you want to get data for
stock=input("Enter a stock symbol: ")
print(stock)

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