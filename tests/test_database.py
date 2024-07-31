import pytest
import os
from src.trading_database import TradingDatabase

@pytest.fixture
def db():
    # Create a temporary database for testing
    db = TradingDatabase(
        transactions_file='test_transactions.json',
        owned_stocks_file='test_owned_stocks.json',
        owned_stocks_history_file='test_owned_stocks_history.json'
    )
    yield db
    # Cleanup after test
    for filename in ['test_transactions.json', 'test_owned_stocks.json', 'test_owned_stocks_history.json']:
        if os.path.exists(filename):
            os.remove(filename)

def test_add_transaction(db):
    transaction_id = db.add_transaction('AAPL', 10, 150.0, 'buy')
    
    assert transaction_id == 1
    assert len(db.list_transactions()) == 1
    assert db.list_transactions()[0] == {
        'id': 1,
        'symbol': 'AAPL',
        'quantity': 10,
        'price': 150.0,
        'transaction_type': 'buy',
        'timestamp': db.list_transactions()[0]['timestamp']
    }
    assert db.list_owned_stocks() == {'AAPL': 10}

def test_update_owned_stocks(db):
    db.add_transaction('AAPL', 10, 150.0, 'buy')
    db.add_transaction('AAPL', 5, 155.0, 'sell')
    
    assert db.list_owned_stocks() == {'AAPL': 5}

def test_record_owned_stocks_history(db):
    # Clear the history before starting the test
    db.owned_stocks_history = []

    db.add_transaction('AAPL', 10, 150.0, 'buy')
    
    # Fetch the history after recording
    history = db.list_owned_stocks_history()
    
    # Ensure that history has the correct number of entries
    assert len(history) == 1  # Should have one entry

    # Check the content of the history
    expected_entry = {
        'owned_stocks': {'AAPL': 10}
    }

    # Compare the historical data without timestamp
    assert history[0]['owned_stocks'] == expected_entry['owned_stocks']

    # Ensure timestamp is present and properly formatted
    assert 'timestamp' in history[0]

def test_save_and_load_transactions(db):
    db.add_transaction('AAPL', 10, 150.0, 'buy')
    db.save_transactions()
    
    new_db = TradingDatabase(
        transactions_file='test_transactions.json',
        owned_stocks_file='test_owned_stocks.json',
        owned_stocks_history_file='test_owned_stocks_history.json'
    )
    
    assert new_db.list_transactions() == db.list_transactions()
    assert new_db.list_owned_stocks() == db.list_owned_stocks()

def test_save_and_load_owned_stocks(db):
    db.add_transaction('AAPL', 10, 150.0, 'buy')
    db.save_owned_stocks()
    
    new_db = TradingDatabase(
        transactions_file='test_transactions.json',
        owned_stocks_file='test_owned_stocks.json',
        owned_stocks_history_file='test_owned_stocks_history.json'
    )
    
    assert new_db.list_owned_stocks() == db.list_owned_stocks()

def test_save_and_load_owned_stocks_history(db):
    db.add_transaction('AAPL', 10, 150.0, 'buy')
    db.record_owned_stocks_history()
    db.save_owned_stocks_history()
    
    new_db = TradingDatabase(
        transactions_file='test_transactions.json',
        owned_stocks_file='test_owned_stocks.json',
        owned_stocks_history_file='test_owned_stocks_history.json'
    )
    
    assert new_db.list_owned_stocks_history() == db.list_owned_stocks_history()
