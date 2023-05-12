# Stock_Ticker
 
Yahoo Finance Ticker Symbols - https://finance.yahoo.com/lookup/

ticker: case insensitive ticker of the desired stock/bond/funds
start_date: date you want the data to start from (mm/dd/yyyy)
end_date: date you want the data to end (mm/dd/yyyy)
index_as_date: {True, False}. Default is true. If true then the dates of the records are set as the index, else they are returned as a separate column.
interval: {“1d”, “1wk”, “1mo”}. Refers to the interval to sample the data: “1d”= daily, “1wk”= weekly, “1mo”=monthly.
