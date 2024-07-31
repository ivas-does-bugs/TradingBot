# TradingDatabase Class Documentation

## Overview

The `TradingDatabase` class provides a simple in-memory trading database with persistent storage capabilities using JSON files. It supports tracking of transactions, currently owned stocks, and historical changes to stock ownership. This class can be used to manage and monitor stock market trading activities.

## Features

- **Manage Transactions**: Add, retrieve, list, and update stock market transactions.
- **Track Owned Stocks**: Maintain the current state of owned stocks.
- **Record Historical Data**: Keep a history of changes to owned stocks.
- **Persistent Storage**: Data is stored in JSON files for persistence across program runs.

## Initialization

```python
TradingDatabase(transactions_file='transactions.json', 
                owned_stocks_file='owned_stocks.json',
                owned_stocks_history_file='owned_stocks_history.json')
```

### 3. Methods


## Methods

### `add_transaction(symbol, quantity, price, transaction_type)`

Adds a new transaction to the database.

#### Parameters

- `symbol` (str): The stock symbol for the transaction (e.g., 'AAPL').
- `quantity` (int): The number of shares involved in the transaction.
- `price` (float): The price per share.
- `transaction_type` (str): The type of transaction ('buy' or 'sell').

#### Returns

- `int`: The ID of the newly added transaction.

### `get_transaction(transaction_id)`

Retrieves a transaction by its ID.

#### Parameters

- `transaction_id` (int): The ID of the transaction to retrieve.

#### Returns

- `dict` or `None`: The transaction details or `None` if not found.

### `list_transactions()`

Lists all transactions.

#### Returns

- `list`: A list of all transactions, where each transaction is represented as a dictionary.

### `list_owned_stocks()`

Lists all currently owned stocks.

#### Returns

- `dict`: A dictionary where keys are stock symbols and values are quantities of shares owned.

### `list_owned_stocks_history()`

Lists the historical records of owned stocks.

#### Returns

- `list`: A list of historical records, each represented as a dictionary containing a timestamp and the state of owned stocks.

### `save_transactions()`

Saves the current state of transactions to the JSON file.

### `load_transactions()`

Loads transactions from the JSON file.

### `save_owned_stocks()`

Saves the current state of owned stocks to the JSON file.

### `load_owned_stocks()`

Loads currently owned stocks from the JSON file.

### `save_owned_stocks_history()`

Saves historical records of owned stocks to the JSON file.

### `load_owned_stocks_history()`

Loads historical records of owned stocks from the JSON file.

## Example Usage

```python
if __name__ == "__main__":
    db = TradingDatabase()
    
    # Add some transactions
    transaction_id1 = db.add_transaction('AAPL', 10, 150.0, 'buy')
    transaction_id2 = db.add_transaction('GOOGL', 5, 2800.0, 'sell')
    transaction_id3 = db.add_transaction('AAPL', 5, 155.0, 'sell')

    # List all transactions
    print("All Transactions:", db.list_transactions())
    
    # Retrieve a transaction
    print("Transaction ID 1:", db.get_transaction(transaction_id1))
    
    # List all currently owned stocks
    print("Currently Owned Stocks:", db.list_owned_stocks())
    
    # List owned stocks history
    print("Owned Stocks History:", db.list_owned_stocks_history())


### 5. Notes

```
## Notes

- **File Paths**: Ensure that the file paths provided during initialization are writable and accessible.
- **Error Handling**: The class handles file not found errors gracefully by initializing with default empty data.
