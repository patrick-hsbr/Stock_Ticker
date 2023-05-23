from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

tickers_file_path = '/Users\patri\Sandbox\Stock_Ticker/tickers.txt'

# Load ticker symbols and company names from tickers.txt
def load_tickers():

    ticker_data = {}
    with open(tickers_file_path, "r") as file:
        for line in file:
            ticker, company = line.strip().split(",")
            ticker_data[ticker] = company
    return ticker_data

# home page with user input form
@app.route("/")
def home():
    ticker_data = load_tickers()
    return render_template("home.html", ticker_data=ticker_data)

# Error page
@app.route("/error")
def error():
    return render_template("error.html")

# result page with chart
@app.route("/response", methods=["POST"])
def response():
    ticker_data = load_tickers()

    # processing user input, asking for a specified stock code/ ticker symbol
    if request.method == "POST":
        ticker_input = request.form["ticker"]
        processed_input = ticker_input.upper()

        # Retrieve data from Yahoo Finance with specified stock code/ ticker symbol
        data = yf.download(processed_input)

        # error handling for user inputs with empty API response
        if data.empty:
            return redirect("/error")

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
                'text': company_name,
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
                    bgcolor="#27374D"
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
            plot_bgcolor='#27374D',
            paper_bgcolor='#27374D',
            font=dict(color='#B3B3B3')
        )

        # Update the y-axis range dynamically based on the visible data
        fig.update_xaxes(rangeslider=dict(visible=True))
        fig.update_layout(xaxis_rangeslider_visible=False)

        # Convert the Plotly figure to HTML and pass it to the template
        chart = fig.to_html(full_html=False)
        return render_template("response.html", chart=chart)

if __name__ == "__main__":
    app.run()