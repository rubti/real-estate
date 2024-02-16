from decimal import Decimal

from mortgage import Loan

from rubti_real_estate.utils import compound_invest, monthly_compound


class RealEstateFinancing:
    def __init__(
        self,
        price,
        incidentals,
        owners_equity,
        interest_rate,
        months: int,
        maintenance_cost,
        inflation=0.02,
        value_increase=0.02,
        alternative_revenue=0.02,
    ) -> None:
        self.loan = Loan(
            price + incidentals - owners_equity,
            interest=interest_rate,
            term=int(months / 12),
            term_unit="years",
            currency="€",
        )
        self.maintenance_cost = Decimal(maintenance_cost)
        self.inflation = Decimal(inflation)
        self.months = months
        self.owners_equity = Decimal(owners_equity)
        self.price = Decimal(price)
        self.value_increase = Decimal(value_increase)
        self.owners_equity = Decimal(owners_equity)
        self.alt_rev = Decimal(alternative_revenue)
        self.currency = "€"

    def total_cost(self):
        cost = self.loan.total_paid
        cost += self.owners_equity
        cost += compound_invest(self.maintenance_cost, self.inflation, self.months)
        return cost

    def end_worth(self):
        return monthly_compound(self.price, self.value_increase, self.months)

    def cost_of_reinvest(self):
        return (
            monthly_compound(self.owners_equity, self.alt_rev, self.months)
            - self.owners_equity
        )

    def total_expense(self):
        return self.total_cost() - self.end_worth()

    def total_expense_with_reinvest_effect(self):
        return self.total_expense() + self.cost_of_reinvest()

    def summarize(self):
        self.loan.summarize
        # fmt: off
        print('Total cost:                   {} {:>11,}'.format(self.currency,self.total_cost()))
        print('Total expenses:               {} {:>11,}'.format(self.currency,self.total_expense()))
        print('Cost of reinvest:             {} {:>11,}'.format(self.currency,self.cost_of_reinvest()))
        print('Total expenses with reinvest: {} {:>11,}'.format(self.currency,self.total_expense_with_reinvest_effect()))
        print('End worth                     {} {:>11,}'.format(self.currency,self.end_worth()))
        # fmt: on
