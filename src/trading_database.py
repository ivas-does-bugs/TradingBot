import json
import datetime

class TradingDatabase:
    def __init__(self, transactions_file='transactions.json', 
                       owned_stocks_file='owned_stocks.json',
                       owned_stocks_history_file='owned_stocks_history.json'):
        self.transactions_file = transactions_file
        self.owned_stocks_file = owned_stocks_file
        self.owned_stocks_history_file = owned_stocks_history_file
        self.transactions = []
        self.owned_stocks = {}
        self.owned_stocks_history = []
        self.transaction_id_counter = 1
        self.load_transactions()
        self.load_owned_stocks()
        self.load_owned_stocks_history()

    def add_transaction(self, symbol, quantity, price, transaction_type):
        """Add a new transaction to the database."""
        transaction = {
            'id': self.transaction_id_counter,
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'transaction_type': transaction_type,  # 'buy' or 'sell'
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.transactions.append(transaction)
        self.transaction_id_counter += 1
        self.save_transactions()
        self.update_owned_stocks(symbol, quantity, transaction_type)
        self.save_owned_stocks()
        self.record_owned_stocks_history()
        return transaction['id']

    def update_owned_stocks(self, symbol, quantity, transaction_type):
        """Update currently owned stocks based on transaction type."""
        if transaction_type == 'buy':
            if symbol in self.owned_stocks:
                self.owned_stocks[symbol] += quantity
            else:
                self.owned_stocks[symbol] = quantity
        elif transaction_type == 'sell':
            if symbol in self.owned_stocks:
                self.owned_stocks[symbol] -= quantity
                if self.owned_stocks[symbol] <= 0:
                    del self.owned_stocks[symbol]

    def record_owned_stocks_history(self):
        """Record the current state of owned stocks in history."""
        print(f"Recording history at: {datetime.datetime.now().isoformat()}")
        self.owned_stocks_history.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'owned_stocks': self.owned_stocks.copy()
        })
        self.save_owned_stocks_history()

    def get_transaction(self, transaction_id):
        """Retrieve a transaction by its ID."""
        for transaction in self.transactions:
            if transaction['id'] == transaction_id:
                return transaction
        return None

    def list_transactions(self):
        """List all transactions."""
        return self.transactions

    def list_owned_stocks(self):
        """List all currently owned stocks."""
        return self.owned_stocks

    def list_owned_stocks_history(self):
        """List all historical records of owned stocks."""
        return self.owned_stocks_history

    def save_transactions(self):
        """Save transactions to the JSON file."""
        with open(self.transactions_file, 'w') as file:
            json.dump({
                'transaction_id_counter': self.transaction_id_counter,
                'transactions': self.transactions
            }, file, indent=4)

    def load_transactions(self):
        """Load transactions from the JSON file."""
        try:
            with open(self.transactions_file, 'r') as file:
                data = json.load(file)
                self.transactions = data.get('transactions', [])
                self.transaction_id_counter = data.get('transaction_id_counter', 1)
        except FileNotFoundError:
            self.transactions = []
            self.transaction_id_counter = 1

    def save_owned_stocks(self):
        """Save currently owned stocks to the JSON file."""
        with open(self.owned_stocks_file, 'w') as file:
            json.dump(self.owned_stocks, file, indent=4)

    def load_owned_stocks(self):
        """Load currently owned stocks from the JSON file."""
        try:
            with open(self.owned_stocks_file, 'r') as file:
                self.owned_stocks = json.load(file)
        except FileNotFoundError:
            self.owned_stocks = {}

    def save_owned_stocks_history(self):
        """Save the historical records of owned stocks to the JSON file."""
        with open(self.owned_stocks_history_file, 'w') as file:
            json.dump(self.owned_stocks_history, file, indent=4)

    def load_owned_stocks_history(self):
        """Load historical records of owned stocks from the JSON file."""
        try:
            with open(self.owned_stocks_history_file, 'r') as file:
                self.owned_stocks_history = json.load(file)
        except FileNotFoundError:
            self.owned_stocks_history = []
