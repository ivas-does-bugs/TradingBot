import pytest
from src.trading_database import TradingDatabase

@pytest.fixture
def db():
    """Fixture to create a fresh database instance for each test."""
    return TradingDatabase()

def test_add_transaction(db):
    """Test adding a transaction."""
    transaction_id = db.add_transaction('AAPL', 10, 150.0, 'buy')
    transaction = db.get_transaction(transaction_id)
    assert transaction is not None
    assert transaction['symbol'] == 'AAPL'
    assert transaction['quantity'] == 10
    assert transaction['price'] == 150.0
    assert transaction['transaction_type'] == 'buy'

def test_list_transactions(db):
    """Test listing transactions."""
    db.add_transaction('AAPL', 10, 150.0, 'buy')
    transactions = db.list_transactions()
    assert len(transactions) > 0