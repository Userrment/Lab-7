from third_func import gender_count
from mock import df


def test_first_class_female():
    choice = 1
    assert gender_count(choice, df)['female'] == 4


def test_first_class_male():
    choice = 1
    assert gender_count(choice, df)['male'] == 6


def test_second_class_female():
    choice = 2
    assert gender_count(choice, df)['female'] == 4


def test_second_class_male():
    choice = 2
    assert gender_count(choice, df)['male'] == 4


def test_third_class_female():
    choice = 3
    assert gender_count(choice, df)['female'] == 17


def test_third_class_male():
    choice = 3
    assert gender_count(choice, df)['male'] == 15
