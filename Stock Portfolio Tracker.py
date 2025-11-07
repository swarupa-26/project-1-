import os

def calculate_portfolio_value(portfolio, stock_prices):
    """
    Calculates the total value of the portfolio.

    Args:
        portfolio (dict): A dictionary where keys are stock symbols and
                          values are the number of shares.
        stock_prices (dict): A dictionary with hardcoded stock prices.
t=
    Returns:
        float: The total value of the investment.
    """
    total_value = 0.0
    print("\n--- Your Portfolio Summary ---")
    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            price = stock_prices[stock]
            stock_value = price * quantity
            total_value += stock_value
            print(f"Stock: {stock}, Quantity: {quantity}, "
                  f"Price/Share: ${price:.2f}, "
                  f"Total Value: ${stock_value:.2f}")
        else:
            print(f"Warning: Stock '{stock}' not found in our price list. "
                  f"It will not be included in the total value calculation.")
    return total_value

def save_portfolio_to_file(portfolio, total_value, filename="portfolio_summary.txt"):
    """
    Saves the portfolio details and total value to a text file.

    Args:
        portfolio (dict): The user's stock portfolio.
        total_value (float): The calculated total investment value.
        filename (str): The name of the file to save.
    """
    with open(filename, 'w') as f:
        f.write("--- Stock Portfolio Summary ---\n\n")
        f.write("Stocks Owned:\n")
        for stock, quantity in portfolio.items():
            f.write(f"- {stock}: {quantity} shares\n")
        f.write("\n")
        f.write(f"Total Investment Value: ${total_value:.2f}\n")
    print(f"\nYour portfolio summary has been saved to '{filename}'.")

def main():
    """
    Main function to run the stock portfolio tracker.
    """
    # Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 188.00,
        "TSLA": 250.00,
        "GOOG": 135.50,
        "AMZN": 140.75,
        "MSFT": 325.00,
        "NVDA": 480.20,
    }

    user_portfolio = {}
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ${price:.2f}")

    while True:
        stock_symbol = input(
            "\nEnter a stock symbol to add (e.g., AAPL) or 'done' to finish: "
        ).upper()
        if stock_symbol == 'DONE':
            break

        if stock_symbol not in stock_prices:
            print(f"Error: '{stock_symbol}' not a valid stock in our list. Please try again.")
            continue

        try:
            quantity = int(input(f"Enter the number of shares for {stock_symbol}: "))
            if quantity < 0:
                print("Error: Quantity must be a positive number.")
                continue
            user_portfolio[stock_symbol] = user_portfolio.get(stock_symbol, 0) + quantity
        except ValueError:
            print("Invalid input. Please enter a whole number for the quantity.")

    if not user_portfolio:
        print("\nNo stocks were added to the portfolio. Exiting.")
        return

    total_investment = calculate_portfolio_value(user_portfolio, stock_prices)
    print(f"\n--- Total Investment Value: ${total_investment:.2f} ---")

    save_option = input(
        "\nWould you like to save this summary to a file? (yes/no): "
    ).lower()
    if save_option == 'yes':
        save_portfolio_to_file(user_portfolio, total_investment)
    else:
        print("Summary not saved. Goodbye!")

if __name__ == "__main__":
    main()
