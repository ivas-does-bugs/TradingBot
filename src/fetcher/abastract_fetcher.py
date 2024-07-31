from abc import ABC, abstractmethod

class FinancialDataFetcher(ABC):

    @abstractmethod
    def fetch_income_statement(self, symbol: str):
        """Fetch and return the income statement for the given stock symbol."""
        pass

    @abstractmethod
    def fetch_balance_sheet(self, symbol: str):
        """Fetch and return the balance sheet for the given stock symbol."""
        pass

    @abstractmethod
    def fetch_stock_price_history(self, symbol: str):
        """Fetch and return historical stock prices and trading volume."""
        pass

    @abstractmethod
    def fetch_news_and_events(self, symbol: str):
        """Fetch and return recent news and events affecting the company."""
        pass

    @abstractmethod
    def fetch_analyst_reports(self, symbol: str):
        """Fetch and return analyst recommendations and brokerage reports."""
        pass

    @abstractmethod
    def set_api_keys(self, api_keys: dict):
        """Set API keys for data sources."""
        pass