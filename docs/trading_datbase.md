# TradingDatabase Documentation

The `TradingDatabase` class provides functionality for managing stock transactions, tracking owned stocks, and maintaining a historical record of transactions and stock ownership. It also handles account balance management.

## Overview

The `TradingDatabase` class includes methods for:
- Adding and managing stock transactions.
- Tracking owned stocks and their purchase prices.
- Calculating the net worth based on current stock prices and account balance.
- Saving and loading data from JSON files.
- Recording historical data including transactions, owned stocks, and account balance.

## Initialization

```python
class TradingDatabase:
    def __init__(self, transactions_file='transactions.json', 
                       owned_stocks_file='owned_stocks.json',
                       owned_stocks_history_file='owned_stocks_history.json',
                       account_balance_file='account_balance.json'):
```

## Parameters

- **`transactions_file`**: Path to the JSON file where transactions are saved.
- **`owned_stocks_file`**: Path to the JSON file where owned stocks are saved.
- **`owned_stocks_history_file`**: Path to the JSON file where historical stock data is saved.
- **`account_balance_file`**: Path to the JSON file where the account balance is saved.

## Methods

### Transaction Management

- **`add_transaction(symbol, quantity, price, transaction_type)`**

  Adds a new transaction to the database. Updates account balance and owned stocks based on the transaction type.

  **Parameters:**
  - **`symbol`**: Stock symbol (e.g., 'AAPL').
  - **`quantity`**: Number of shares bought or sold.
  - **`price`**: Price per share.
  - **`transaction_type`**: Type of transaction ('buy' or 'sell').

  **Returns:**
  - Transaction ID.

- **`get_transaction(transaction_id)`**

  Retrieves a transaction by its ID.

  **Parameters:**
  - **`transaction_id`**: The ID of the transaction to retrieve.

  **Returns:**
  - The transaction object or `None` if not found.

- **`list_transactions()`**

  Lists all transactions.

  **Returns:**
  - A list of transactions.

### Stock Management

- **`update_owned_stocks(symbol, quantity, price, transaction_type)`**

  Updates currently owned stocks based on the transaction type.

  **Parameters:**
  - **`symbol`**: Stock symbol.
  - **`quantity`**: Number of shares.
  - **`price`**: Purchase price per share.
  - **`transaction_type`**: Type of transaction ('buy' or 'sell').

- **`list_owned_stocks()`**

  Lists all currently owned stocks and their quantities.

  **Returns:**
  - A dictionary of owned stocks with quantities and purchase prices.

- **`record_owned_stocks_history()`**

  Records the current state of owned stocks and account balance in history.

- **`list_owned_stocks_history()`**

  Lists all historical records of owned stocks and account balance.

  **Returns:**
  - A list of historical records.

### Financial Management

- **`calculate_net_worth(current_prices)`**

  Calculates the total net worth based on current stock prices and account balance.

  **Parameters:**
  - **`current_prices`**: Dictionary of current stock prices keyed by symbol.

  **Returns:**
  - Total net worth.

### Data Persistence

- **`save_transactions()`**

  Saves transactions to the JSON file.

- **`load_transactions()`**

  Loads transactions from the JSON file.

- **`save_owned_stocks()`**

  Saves currently owned stocks to the JSON file.

- **`load_owned_stocks()`**

  Loads currently owned stocks from the JSON file.

- **`save_owned_stocks_history()`**

  Saves the historical records of owned stocks and account balance to the JSON file.

- **`load_owned_stocks_history()`**

  Loads historical records of owned stocks and account balance from the JSON file.

- **`save_account_balance()`**

  Saves the account balance to the JSON file.

- **`load_account_balance()`**

  Loads the account balance from the JSON file.

## Example Usage

# Create a TradingDatabase instance
db = TradingDatabase()

# Add a transaction
transaction_id = db.add_transaction('AAPL', 10, 150.0, 'buy')

# List all transactions
transactions = db.list_transactions()

# Update owned stocks
db.update_owned_stocks('AAPL', 10, 150.0, 'buy')

# Calculate net worth
current_prices = {'AAPL': 160.0}
net_worth = db.calculate_net_worth(current_prices)

# Record and list owned stocks history
db.record_owned_stocks_history()
history = db.list_owned_stocks_history()

## Notes
Ensure that the data directory exists or will be created in the root folder where the script is run.
Handle exceptions for insufficient balance or invalid transactions where appropriate.