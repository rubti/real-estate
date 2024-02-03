from decimal import Decimal


def quantize_decimal(value: Decimal) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"))


def compound_price(price: Decimal, annual_increase: Decimal, months: int):
    """Compound price increase considering monthly intervals"""
    return price * (1 + annual_increase / 12) ** months


def compound_invest(invest: Decimal, annual_interest: Decimal, months: int) -> Decimal:
    results = []
    for m in range(months):
        results.append(compound_price(invest, annual_interest, months - m))
    return sum(results)


def rate_of_return(investment: Decimal, revenue: Decimal):
    return (revenue - investment) / investment
