from abc import ABC, abstractmethod

class BaseDecisionMaker(ABC):
    
    @abstractmethod
    def analyze_financial_data(self, symbol: str, income_statement: dict, balance_sheet: dict, stock_price_history: dict):
        """
        Analyze financial data and return key metrics.
        """
        pass

    @abstractmethod
    def analyze_news(self, symbol: str, recent_news: list):
        """
        Analyze news and qualitative factors affecting the company.
        """
        pass

    @abstractmethod
    def generate_recommendations(self, symbol: str, metrics: dict, news_analysis: dict):
        """
        Generate investment recommendations based on financial metrics and news analysis.
        """
        pass