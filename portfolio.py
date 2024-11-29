import random
from datetime import datetime

class Stock:
    def __init__(self, name: str):
        self.name = name
    
    def price(self, date: datetime):
        "Almost always prices are > 0 value, always possitive value I hope hahah."
        return random.randint(1, 100)


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.assets = {}
        self.last_return = None
        self.last_annualized_return = None
        self.last_initial_value = None
        self.last_final_value = None
        self.last_profit = None
        self.last_annualized_profit = None


    def add_stock(self, stock: Stock, quantity: float):
        if self.assets.get(stock.name):
            self.assets[stock.name][1] += quantity
        else:
            self.assets[stock.name] = [stock, quantity]
    
    def value_at_date(self, date: datetime) -> float:
        return sum(
            asset[0].price(date) * asset[1] for asset in self.assets.values()
        )

    def profit(self, init_date, final_date) -> float:
        """
        Return = final value of portfolio / initial value of portfolio - 1
        Profit = Initial Capital * Return
        """
        if init_date > final_date:
            raise ValueError("Final Date has to be greater than Init Date")
        final_value = self.value_at_date(final_date)
        initial_value = self.value_at_date(init_date)
        ret = (final_value / initial_value) - 1
        profit = initial_value * ret

        #Persist information
        self.last_return = ret
        self.last_annualized_return = self.annualized_return(ret, init_date, final_date)
        self.last_initial_value = initial_value
        self.last_final_value = final_value
        self.last_init_date = init_date
        self.last_final_date = final_date
        self.last_profit = profit
        self.last_annualized_profit = self.last_annualized_return * self.last_initial_value

        return profit
    
    def annualized_return(self, ret, init_date: datetime, final_date: datetime):
        days = (final_date - init_date).days
        if days < 0:
            raise ValueError("Init Date has to be greater than final date")
        annual_return = (1 + ret) ** (365/ days) - 1
        return annual_return
    

def format_return(profit: float) -> float:
    "Percent 0 to 100 value of profit"
    return round(profit * 100, 2)

def make_random_portfolio():
    stocks = [
        ['Zoro', 5],
        ['Namy', 1], 
        ['Sanji', 2],
        ['Luffy', 3],
        ['Namy', 4],
    ]
    portfolio = Portfolio("Muguiwara")
    for stock in stocks:
        portfolio.add_stock(
            stock=Stock(stock[0]),
            quantity=stock[1]
        )
    return portfolio


DATE_FORMAT = "%d/%m/%Y"

if __name__ == '__main__':
    init_date = datetime(year=2024, month=11, day=1)
    final_date = datetime(year=2024, month=11, day=28)
    portfolio = make_random_portfolio()
    
    profit = portfolio.profit(init_date, final_date)
    annual_profit = portfolio.last_annualized_profit

    print(
        f"""
        The portafolio {portfolio.name}:
        Has an initial capital amount of: ${portfolio.last_initial_value:.2f}.
        Has a final capital amount of: ${portfolio.last_final_value:.2f}.
        Has a proft of : {profit:.2f} u.
        The return between {init_date.strftime(DATE_FORMAT)} and {final_date.strftime(DATE_FORMAT)} is: {format_return(portfolio.last_return)}%
        This is equivalent to a annual return of {format_return(portfolio.last_annualized_return)}%.
        """
    )
