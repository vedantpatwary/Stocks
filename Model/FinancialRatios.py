class FinancialRatios:
    """Class to store and manage financial ratios of a company."""
    def __init__(self, data):
        self.current_price = data.get("Current Price")
        self.market_cap = data.get("Mar Cap")
        self.pe = data.get("Price to Earning")
        self.industry_pe = data.get("Industry PE")
        self.roce = data.get("ROCE")
        self.return_on_equity = data.get("Return on equity")
        self.profit_var_5yrs = data.get("Profit Var 5Yrs")
        self.profit_after_tax = data.get("Profit after tax")
        self.price_to_book = data.get("Price to book value")
        self.promoter_holding = data.get("Promoter holding")
        self.debt_to_equity = data.get("Debt to equity")
        self.sales_growth_5yrs = data.get("Sales growth 5Years")
        self.sales_growth_3yrs = data.get("Sales growth 3Years")
        self.from_52w_high = data.get("From 52w high")
        self.qoq_profits = data.get("QoQ Profits")
        self.qtr_profit_var = data.get("Qtr Profit Var")

    def to_dict(self):
        """Convert the object to a JSON-serializable dictionary."""
        return {key: value for key, value in self.__dict__.items() if value is not None}


    def __str__(self):
        """Returns formatted financial ratios"""
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items() if value is not None])
