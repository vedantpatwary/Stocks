class FinancialRatios:
    """Class to store and manage financial ratios of a company."""
    def __init__(self, data):
        self.profit_var_5yrs = data.get("Profit Var 5Yrs")
        self.profit_after_tax = data.get("Profit after tax")
        self.price_to_book = data.get("Price to book value")
        self.industry_pe = data.get("Industry PE")
        self.debt = data.get("Debt")
        self.promoter_holding = data.get("Promoter holding")
        self.debt_to_equity = data.get("Debt to equity")
        self.no_of_shares = data.get("No. Eq. Shares")
        self.roce = data.get("ROCE")
        self.sales_growth_5yrs = data.get("Sales growth 5Years")
        self.from_52w_high = data.get("From 52w high")
        self.high_price = data.get("High price")
        self.up_from_52w_low = data.get("Up from 52w low")
        self.down_from_52w_high = data.get("Down from 52w high")
        self.qoq_profits = data.get("QoQ Profits")
        self.market_cap = data.get("Mar Cap")
        self.current_price = data.get("Current Price")
        self.price_to_earning = data.get("Price to Earning")

    def to_dict(self):
        """Convert the object to a JSON-serializable dictionary."""
        return {key: value for key, value in self.__dict__.items() if value is not None}


    def __str__(self):
        """Returns formatted financial ratios"""
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items() if value is not None])
