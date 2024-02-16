from dataclasses import dataclass
from decimal import Decimal


class InvestWithRent:
    def __init__(
        self,
        monthly_rent: Decimal,
        monthly_income: Decimal,
        monthly_expenses: Decimal,
        interest: Decimal,
        months: int,
        currency: str = "€",
    ):
        self.monthly_rent = monthly_rent
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.interest = interest
        self.months = months
        self.to_invest: Decimal = monthly_income - monthly_rent - monthly_expenses
        self.investment: Decimal = self.months * self.to_invest
        self.currency = currency

    def compound_revenue(self):
        return compound_invest(self.to_invest, self.interest, self.months)

    def rate_of_return(self):
        return (self.compound_revenue() - self.investment) / self.investment

    # fmt: off
    def summarize(self):
        print('Monthly Investment       {} {:>11,}'.format(self.currency,self.to_invest))
        print('Annual Interest Rate:       {:>11} %'.format(self.interest * 100))
        print('Term (months):              {:>11}'.format(self.months))
        print('Compound revenue:        {} {:>11,}'.format(self.currency,self.compound_revenue()))
        print('Investment:              {} {:>11,}'.format(self.currency,self.investment))
        print('Interests:               {} {:>11,}'.format(self.currency,self.compound_revenue()-self.investment))
        print('Rate of Return:             {:>11} %'.format(self.rate_of_return() * 100))
    # fmt: on
