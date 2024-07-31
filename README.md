# SillyProject

SillyProject is a financial analysis tool that integrates data fetching and decision-making components to analyze stock data. It includes features for fetching financial statements, calculating financial ratios, handling historical data, integrating market data, and analyzing qualitative factors.

## Project Structure

- **`src/`**: Contains the core source code of the project.
  - **`trading_database.py`**: Manages the storage and retrieval of trading data.
  - **`trading_bot.py`**: Defines the `FinancialBot` class that uses fetchers and decision makers.
  - **`fetcher/`**: Contains modules for fetching data from various APIs.
    - **`financial_data_fetcher.py`**: Abstract base class for financial data fetchers.
    - **`alpha_vantage_fetcher.py`**: Fetcher implementation for Alpha Vantage API.
    - **`news_api_fetcher.py`**: Example fetcher for news API (if used).
  - **`decision_maker/`**: Contains modules for decision-making logic.
    - **`simple_decision_maker.py`**: Implements a basic decision-making strategy.
    - **`advanced_decision_maker.py`**: Placeholder for more complex decision-making strategies.
  - **`bot.py`**: Integrates fetchers and decision makers into a coherent bot.

- **`tests/`**: Contains unit tests for the project.
  - **`test_database.py`**: Tests for the trading database functionalities.
  - **`test_fetcher.py`**: Tests for the data fetcher components.
  - **`test_decision_maker.py`**: Tests for the decision-making components.
  - **`test_bot.py`**: Integration tests for the financial bot.

- **`.gitignore`**: Specifies files and directories to be ignored by Git.

- **`requirements.txt`**: Lists the project dependencies.
