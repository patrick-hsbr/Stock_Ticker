from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

# home page with user input form
@app.route("/")
def home():
    return render_template("home.html")

# result page with chart
@app.route("/index", methods=["POST"])
def index():
    
     # processing user input, asking for a specified stock code/ ticker symbol  
     if request.method == "POST":
        user_input = request.form["text"]
        processed_input = user_input.upper()
        
        # Retrieve data from Yahoo Finance with specified stock code/ ticker symbol
        data = yf.download(processed_input)
        
        # error handling for user inputs with empty api response
        if data.empty:
            return "Error: No data available for the specified code/ ticker symbol."
        
        # retrieving company information "longName" for specified stock code/ ticker symbol
        yticker = yf.Ticker(processed_input)
        company_name = yticker.info["longName"]

        # Create a new Plotly figure with a candlestick trace
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            increasing=dict(line=dict(color='#00ff7f')),
            decreasing=dict(line=dict(color='#ff6347'))
        )])

        # Set the chart layout with some style and a range slider
        fig.update_layout(
            title={
                'text': company_name + " in USD",
                'font': {
                    'size': 22,
                    'color': '#B3B3B3'
                }
                
            },
            xaxis=dict(
                title="Date",
                tickformat='%d/%m/%Y',
                showgrid=False,
                rangeselector=dict(
                    buttons=list([
                        dict(count=7, label="1w", step="day", stepmode="backward"),
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ]),
                    bgcolor="#404040" # Add this line to change the background color to white
                ),
                rangeslider=dict(
                    visible=True,
                    thickness=0.1
                ),
                type="date"
            ),
            yaxis=dict(
                title="Price (USD)",
                tickprefix="$",
                showgrid=False
            ),
            margin=dict(l=60, r=60, t=100, b=40),
            plot_bgcolor='#202020',
            paper_bgcolor='#202020',
            font=dict(color='#B3B3B3')
        )

        # Update the y-axis range dynamically based on the visible data
        fig.update_xaxes(rangeslider=dict(visible=True))
        fig.update_layout(xaxis_rangeslider_visible=False)

        # Convert the Plotly figure to HTML and pass it to the template
        chart = fig.to_html(full_html=False)
        return render_template("index.html", chart=chart)

if __name__ == "__main__":
    app.run()
    
