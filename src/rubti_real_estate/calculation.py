from rubti_real_estate.real_estate import RealEstateFinancing
from rubti_real_estate.utils import compound_invest, monthly_compound, rate_of_return

net_monthly_income = 3489
monthly_costs = 1929.63
budget_bea = 500
rent = 1300
investment_months = 18 * 12
k = 1000
owners_equity = 100 * k
compound_owners_equity = monthly_compound(owners_equity, 0.02, investment_months)

rent_invest = InvestWithRent(
    rent, net_monthly_income + budget_bea, monthly_costs, 0.035, investment_months
)

real_estate = RealEstateFinancing(
    320 * k, 30 * k, owners_equity, 0.04, investment_months, (20 * 80) / 12
)

print("---Rent---")
print("==========")
rent_invest.summarize()
print("")
print(f"Considering compound interests of owners equity of {owners_equity}")
print(f"Compound Interests: {compound_owners_equity}")
print(
    f"Total revenue: {rent_invest.compound_revenue() + compound_owners_equity - owners_equity}"
)
print("")
print("---Investment---")
print("================")
real_estate.summarize()
