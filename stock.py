import requests

API_KEY = 'YOUR_FINANCIAL_API_KEY'  # Replace with your API key
BASE_URL = 'https://api.example.com/v1'  # Replace with the actual API endpoint

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks and self.stocks[symbol] >= quantity:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] == 0:
                del self.stocks[symbol]
            print(f"Removed {quantity} shares of {symbol}.")
        else:
            print("Not enough shares to remove.")

    def get_stock_price(self, symbol):
        response = requests.get(f"{BASE_URL}/quote?symbol={symbol}&apikey={API_KEY}")
        if response.status_code == 200:
            data = response.json()
            return data['latestPrice']
        else:
            print("Error fetching stock price.")
            return None

    def display_portfolio(self):
        print("Your Stock Portfolio:")
        for symbol, quantity in self.stocks.items():
            price = self.get_stock_price(symbol)
            print(f"{symbol}: {quantity} shares at ${price:.2f} each" if price else f"{symbol}: {quantity} shares")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.display_portfolio()
    portfolio.remove_stock("AAPL", 5)
    portfolio.display_portfolio()