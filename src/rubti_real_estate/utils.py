from decimal import Decimal


def continuous_compound(
    amount: Decimal, annual_growths: Decimal, years: Decimal
) -> Decimal:
    """
    Classic continuos compound calculation

    Args:
        amount (Decimal): Initial amount
        annual_growths (Decimal): Annual growths in percent (4% = 0.04)
        years (Decimal): Time span in years over which the annual growths shall
        be calculated

    Returns:
        Decimal: Amount after the given time span
    """
    return amount * Decimal(annual_growths * years).exp()


def monthly_compound(
    amount: Decimal, annual_growths: Decimal, years: Decimal
) -> Decimal:
    """Compound price increase considering monthly intervals"""
    return amount * (1 + annual_growths / 12) ** (years * 12)


def yearly_compound(
    amount: Decimal, annual_growths: Decimal, years: Decimal
) -> Decimal:
    """Compound interests considering yearly compound"""
    return amount * (1 + annual_growths) ** years


def compound_invest(invest: Decimal, annual_interest: Decimal, months: int) -> Decimal:
    results = []
    for m in range(months):
        results.append(monthly_compound(invest, annual_interest, months - m))
    return sum(results)


def rate_of_return(investment: Decimal, revenue: Decimal):
    return (revenue - investment) / investment


def sum_monthly_amount_yearly_compound(
    monthly_cost: Decimal, annual_increase: Decimal, years: int, months: int
) -> Decimal:
    current_cost = monthly_cost
    result = []
    for y in range(years):
        result.append(current_cost * 12)
        current_cost *= 1 + annual_increase
    result.append(current_cost * months)
    return sum(result)
