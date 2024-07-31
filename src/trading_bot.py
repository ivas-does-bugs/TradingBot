from .trading_database import TradingDatabase

def main():
    """Main function to run the trading bot."""
    # Initialize the TradingDatabase
    db = TradingDatabase()

    # Example: Add some transactions
    transaction_id1 = db.add_transaction('AAPL', 10, 150.0, 'buy')
    transaction_id2 = db.add_transaction('GOOGL', 5, 2800.0, 'sell')
    transaction_id3 = db.add_transaction('AAPL', 5, 155.0, 'sell')

    # Print all transactions
    print("All Transactions:", db.list_transactions())
    
    # Print a specific transaction
    print("Transaction ID 1:", db.get_transaction(transaction_id1))
    
    # Print currently owned stocks
    print("Currently Owned Stocks:", db.list_owned_stocks())
    
    # Print historical records of owned stocks
    print("Owned Stocks History:", db.list_owned_stocks_history())

if __name__ == "__main__":
    main()