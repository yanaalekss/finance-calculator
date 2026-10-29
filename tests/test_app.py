import pytest

from app import FinanceCalculator


def test_add_income():
    calculator = FinanceCalculator()
    calculator.add_income(10000)

    assert calculator.total_income() == 10000


def test_add_expense():
    calculator = FinanceCalculator()
    calculator.add_expense(3000)

    assert calculator.total_expenses() == 3000


def test_balance():
    calculator = FinanceCalculator()
    calculator.add_income(10000)
    calculator.add_expense(3000)

    assert calculator.balance() == 7000


def test_empty_balance():
    calculator = FinanceCalculator()

    assert calculator.balance() == 0


def test_negative_income():
    calculator = FinanceCalculator()

    with pytest.raises(ValueError):
        calculator.add_income(-100)


def test_zero_expense():
    calculator = FinanceCalculator()

    with pytest.raises(ValueError):
        calculator.add_expense(0)

#def test_failure_example():
#    assert 1 == 2