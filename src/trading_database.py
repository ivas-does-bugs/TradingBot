import json
import datetime
import os

class TradingDatabase:
    def __init__(self, transactions_file='transactions.json', 
                       owned_stocks_file='owned_stocks.json',
                       owned_stocks_history_file='owned_stocks_history.json',
                       account_balance_file='account_balance.json'):
        # Define the directory and file paths
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.transactions_file = os.path.join(self.data_dir, transactions_file)
        self.owned_stocks_file = os.path.join(self.data_dir, owned_stocks_file)
        self.owned_stocks_history_file = os.path.join(self.data_dir, owned_stocks_history_file)
        self.account_balance_file = os.path.join(self.data_dir, account_balance_file)

        # Ensure the data directory exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.transactions = []
        self.owned_stocks = {}  # {symbol: {'quantity': int, 'purchase_price': float}}
        self.owned_stocks_history = []
        self.transaction_id_counter = 1
        self.account_balance = 0.0  # Initialize account balance

        self.load_transactions()
        self.load_owned_stocks()
        self.load_owned_stocks_history()
        self.load_account_balance()

    def validate_transaction(self, symbol, quantity, price, transaction_type):
        """Validate input values."""
        if not symbol or quantity <= 0 or price <= 0 or transaction_type not in ['buy', 'sell']:
            raise ValueError("Invalid input values: Symbol, quantity, and price must be positive. Transaction type must be 'buy' or 'sell'.")

    def add_transaction(self, symbol, quantity, price, transaction_type):
        """Add a new transaction to the database."""
        self.validate_transaction(symbol, quantity, price, transaction_type)
        
        if transaction_type == 'buy':
            total_cost = quantity * price
            if total_cost > self.account_balance:
                raise ValueError("Insufficient account balance to complete the transaction.")
            self.account_balance -= total_cost
        elif transaction_type == 'sell':
            if symbol not in self.owned_stocks or quantity > self.owned_stocks[symbol]['quantity']:
                raise ValueError("Insufficient stock quantity to complete the transaction.")
            total_income = quantity * price
            self.account_balance += total_income

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
        self.update_owned_stocks(symbol, quantity, price, transaction_type)
        self.save_owned_stocks()
        self.record_owned_stocks_history()
        self.save_account_balance()
        return transaction['id']

    def update_owned_stocks(self, symbol, quantity, price, transaction_type):
        """Update currently owned stocks based on transaction type."""
        self.validate_transaction(symbol, quantity, price, transaction_type)
        
        if transaction_type == 'buy':
            if symbol in self.owned_stocks:
                current_quantity = self.owned_stocks[symbol]['quantity']
                current_purchase_price = self.owned_stocks[symbol]['purchase_price']
                # Update quantity and average purchase price
                total_cost = current_quantity * current_purchase_price
                new_total_cost = total_cost + (quantity * price)
                new_quantity = current_quantity + quantity
                new_purchase_price = new_total_cost / new_quantity
                self.owned_stocks[symbol] = {'quantity': new_quantity, 'purchase_price': new_purchase_price}
            else:
                self.owned_stocks[symbol] = {'quantity': quantity, 'purchase_price': price}
        elif transaction_type == 'sell':
            if symbol in self.owned_stocks:
                current_quantity = self.owned_stocks[symbol]['quantity']
                if quantity >= current_quantity:
                    del self.owned_stocks[symbol]
                else:
                    self.owned_stocks[symbol]['quantity'] -= quantity

    def record_owned_stocks_history(self):
        """Record the current state of owned stocks and account balance in history."""
        print(f"Recording history at: {datetime.datetime.now().isoformat()}")
        self.owned_stocks_history.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'owned_stocks': self.owned_stocks.copy(),
            'account_balance': self.account_balance  # Record the account balance
        })
        self.save_owned_stocks_history()

    def calculate_net_worth(self, current_prices):
        """Calculate the total net worth based on current stock prices and account balance."""
        net_worth = self.account_balance
        for symbol, stock in self.owned_stocks.items():
            if symbol in current_prices:
                net_worth += stock['quantity'] * current_prices[symbol]
        return net_worth

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
        """List all historical records of owned stocks and account balance."""
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
        """Save the historical records of owned stocks and account balance to the JSON file."""
        with open(self.owned_stocks_history_file, 'w') as file:
            json.dump(self.owned_stocks_history, file, indent=4)

    def load_owned_stocks_history(self):
        """Load historical records of owned stocks and account balance from the JSON file."""
        try:
            with open(self.owned_stocks_history_file, 'r') as file:
                self.owned_stocks_history = json.load(file)
        except FileNotFoundError:
            self.owned_stocks_history = []

    def save_account_balance(self):
        """Save the account balance to the JSON file."""
        with open(self.account_balance_file, 'w') as file:
            json.dump({'account_balance': self.account_balance}, file, indent=4)

    def load_account_balance(self):
        """Load the account balance from the JSON file."""
        try:
            with open(self.account_balance_file, 'r') as file:
                data = json.load(file)
                self.account_balance = data.get('account_balance', 0.0)
        except FileNotFoundError:
            self.account_balance = 0.0

    def add_account_balance(self, amount):
        """Add money to the account balance."""
        if amount <= 0:
            raise ValueError("Amount to add must be positive.")
        self.account_balance += amount
        self.save_account_balance()

    def remove_account_balance(self, amount):
        """Remove money from the account balance."""
        if amount <= 0:
            raise ValueError("Amount to remove must be positive.")
        if amount > self.account_balance:
            raise ValueError("Insufficient account balance.")
        self.account_balance -= amount
        self.save_account_balance()

    def get_account_balance(self):
        """Get account balance"""
        return self.account_balance

    def clear_transactions(self):
        """Clear all transactions."""
        self.transactions = []
        self.transaction_id_counter = 1
        self.save_transactions()

    def clear_owned_stocks(self):
        """Clear owned stocks."""
        self.owned_stocks = {}
        self.save_owned_stocks()

    def clear_owned_stocks_history(self):
        """Clear owned stocks history."""
        self.owned_stocks_history = []
        self.save_owned_stocks_history()

    def reset_account_balance(self):
        """Reset the account balance to zero."""
        self.account_balance = 0.0
        self.save_account_balance()