"""Unit tests for compounding calculations"""

from decimal import Decimal as D

from rubti_real_estate.utils import (
    continuous_compound,
    sum_monthly_amount_yearly_compound,
)


def test_compound():
    quant = D("0.00001")
    excepted_result = D("738.9056098930650227230427461")
    assert continuous_compound(D("100"), D("0.04"), D("50")).quantize(
        quant
    ) == excepted_result.quantize(quant)


def test_sum_monthly():
    quant = D("0.01")
    expected_result = D("378231.46")
    assert (
        sum_monthly_amount_yearly_compound(D("1440"), D("0.02"), 18, 4).quantize(quant)
        == expected_result
    )
