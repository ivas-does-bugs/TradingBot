class MathematicalTools:
    
    @staticmethod
    def calculate_valuation_ratios(income_statement: dict, stock_price_history: dict):
        """
        Calculate financial ratios such as P/E Ratio.
        """
        earnings = income_statement.get('net_income', 0)
        price = stock_price_history.get('current_price', 1)  # Avoid division by zero
        pe_ratio = price / (earnings / 1e6)  # Adjust earnings as needed
        return {'P/E Ratio': pe_ratio}
    
    @staticmethod
    def calculate_profitability_ratios(balance_sheet: dict):
        """
        Calculate profitability ratios such as ROE.
        """
        net_income = balance_sheet.get('net_income', 0)
        shareholder_equity = balance_sheet.get('shareholder_equity', 1)  # Avoid division by zero
        roe = net_income / shareholder_equity
        return {'ROE': roe}
