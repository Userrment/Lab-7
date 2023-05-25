from first_func import avg_price
from mock import df


def test_not_survived():
    choice = 0
    assert round(avg_price(choice, df), 2) == 29.14


def test_survived():
    choice = 1
    assert round(avg_price(choice, df), 2) == 26.31
