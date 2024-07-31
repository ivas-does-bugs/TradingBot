import gradio as gr
import pandas as pd
from trading_database import TradingDatabase

# Initialize the trading database
db = TradingDatabase()

def buy_stock(symbol, quantity, price):
    try:
        transaction_id = db.add_transaction(symbol, quantity, price, 'buy')
        return f"Bought {quantity} of {symbol} at ${price} each. Transaction ID: {transaction_id}"
    except ValueError as e:
        return str(e)

def sell_stock(symbol, quantity, price):
    try:
        transaction_id = db.add_transaction(symbol, quantity, price, 'sell')
        return f"Sold {quantity} of {symbol} at ${price} each. Transaction ID: {transaction_id}"
    except ValueError as e:
        return str(e)

def view_data(database):
    """Fetch data from the selected database and return it as a pandas DataFrame."""
    if database == "Transactions":
        data = db.list_transactions()
        df = pd.DataFrame(data)
    elif database == "Owned Stocks":
        data = db.list_owned_stocks()
        df = pd.DataFrame.from_dict(data, orient='index').reset_index().rename(columns={'index': 'Symbol'})
    elif database == "Owned Stocks History":
        data = db.list_owned_stocks_history()
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame()  # Empty DataFrame for unsupported databases
    return df

def add_balance(amount):
    try:
        db.add_account_balance(amount)
        return f"Account balance updated by ${amount}. New balance: ${db.get_account_balance()}"
    except ValueError as e:
        return str(e)

def remove_balance(amount):
    try:
        db.remove_account_balance(amount)
        return f"Account balance decreased by ${amount}. New balance: ${db.get_account_balance()}"
    except ValueError as e:
        return str(e)

def clear_data(data_type):
    """Clear data based on the selected type."""
    if data_type == "Transactions":
        db.clear_transactions()
        return "Transactions cleared."
    elif data_type == "Owned Stocks":
        db.clear_owned_stocks()
        return "Owned stocks cleared."
    elif data_type == "Owned Stocks History":
        db.clear_owned_stocks_history()
        return "Owned stocks history cleared."
    elif data_type == "All Data":
        db.clear_transactions()
        db.clear_owned_stocks()
        db.clear_owned_stocks_history()
        db.reset_account_balance()  # Reset account balance to zero
        return "All data cleared and balance reset."
    else:
        return "Invalid selection."

def update_balance_label():
    """Update the balance label with the current account balance."""
    return f"Current Balance: ${db.get_account_balance()}"

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Trading Bot Interface")

        # Display current balance
        with gr.Row():
            balance_label = gr.Label(value=update_balance_label(), elem_id="balance_label")

        with gr.Tab("Trade"):
            with gr.Row():
                symbol_input = gr.Textbox(label="Symbol")
                quantity_input = gr.Number(label="Quantity", step=1, minimum=1)
                price_input = gr.Number(label="Price", step=0.01, minimum=0.01)
                
            with gr.Row():
                buy_button = gr.Button("Buy")
                sell_button = gr.Button("Sell")
                
            buy_output = gr.Textbox(label="Buy Status")
            sell_output = gr.Textbox(label="Sell Status")
            
            buy_button.click(lambda symbol, qty, price: (buy_stock(symbol, qty, price), update_balance_label()), 
                             inputs=[symbol_input, quantity_input, price_input], 
                             outputs=[buy_output, balance_label])
            sell_button.click(lambda symbol, qty, price: (sell_stock(symbol, qty, price), update_balance_label()), 
                              inputs=[symbol_input, quantity_input, price_input], 
                              outputs=[sell_output, balance_label])

        with gr.Tab("View Data"):
            database_selector = gr.Dropdown(
                choices=["Transactions", "Owned Stocks", "Owned Stocks History"],
                label="Select Database"
            )
            data_output = gr.Dataframe(headers=["ID", "Symbol", "Quantity", "Price", "Timestamp"], value=[], type="pandas")
            
            database_selector.change(view_data, inputs=database_selector, outputs=data_output)

        with gr.Tab("Account Balance"):
            balance_input = gr.Number(label="Amount to Add", step=0.01, minimum=0)
            add_balance_button = gr.Button("Add Balance")
            remove_balance_input = gr.Number(label="Amount to Remove", step=0.01, minimum=0)
            remove_balance_button = gr.Button("Remove Balance")
            balance_output = gr.Textbox(label="Balance Status")
            
            add_balance_button.click(lambda amount: (add_balance(amount), update_balance_label()), 
                                     inputs=balance_input, 
                                     outputs=[balance_output, balance_label])
            remove_balance_button.click(lambda amount: (remove_balance(amount), update_balance_label()), 
                                        inputs=remove_balance_input, 
                                        outputs=[balance_output, balance_label])
        
        with gr.Tab("Delete Data"):
            data_selector = gr.Dropdown(
                choices=["Transactions", "Owned Stocks", "Owned Stocks History", "All Data"],
                label="Select Data to Delete"
            )
            delete_button = gr.Button("Delete Data")
            delete_output = gr.Textbox(label="Delete Status")
            
            delete_button.click(lambda data_type: (clear_data(data_type), update_balance_label()), 
                                inputs=data_selector, 
                                outputs=[delete_output, balance_label])
        
        # Update balance label on interface load
        demo.load(lambda: update_balance_label())

    demo.launch()

if __name__ == "__main__":
    create_interface()
