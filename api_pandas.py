import requests
import pandas as pd

# Define API URL and parameters
url = "https://www.alphavantage.co/query"
params = {
    "function": "NEWS_SENTIMENT",
    "tickers": "AAPL",
    "apikey": "demo"
}

# Fetch data from API
response = requests.get(url, params=params)
data = response.json()

# Extract news articles
if "feed" in data:
    articles = data["feed"]

    # Create DataFrame
    df = pd.DataFrame(articles, columns=["title", "summary"])
    print(df)
else:
    print("No data found or API limit reached.")
