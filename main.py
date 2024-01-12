 
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import requests

# Create a Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def index():
    # Render the index.html file
    return render_template('index.html')

# Define the route for the data request
@app.route('/data')
def get_data():
    # Fetch stock data from an external source (e.g., Yahoo Finance API)
    # Here, we are using a sample API for demonstration purposes
    url = 'https://query1.finance.yahoo.com/v7/finance/quote?symbols=GOOG,AAPL'
    response = requests.get(url)
    data = response.json()

    # Extract the necessary data from the API response
    stock_data = []
    for stock in data['quoteResponse']['result']:
        stock_data.append({
            'symbol': stock['symbol'],
            'price': stock['regularMarketPrice'],
            'change': stock['regularMarketChange'],
            'change_percent': stock['regularMarketChangePercent']
        })

    # Return the stock data in JSON format
    return jsonify(stock_data)

# Define the route for the about page
@app.route('/about')
def about():
    # Render the about.html file
    return render_template('about.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
