 # Stock Portfolio Tracker

print("📊 Welcome to Stock Portfolio Tracker")

portfolio = {}
total_investment = 0

# predefined stock prices (can be updated)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320,
    "AMZN": 135
}

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("⚠ Stock not found! Try again.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except:
        print("❌ Invalid input! Enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# calculation
print("\n📈 Your Portfolio Summary:")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    
    print(f"{stock} -> {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")