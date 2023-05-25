from second_func import avg_age
from mock import df


def test_first_class():
    choice = 1
    assert round(avg_age(choice, df), 2) == 38.0


def test_second_class():
    choice = 2
    assert round(avg_age(choice, df), 2) == 33.43


def test_third_class():
    choice = 3
    assert round(avg_age(choice, df), 2) == 20.65
