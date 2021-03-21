from practical_stu import *


def test_gcd():
    num1 = 12
    num2 = 4

    excepted = 4
    actual = gcd(num1, num2)

    assert excepted == actual


def test_is_palidrome():
    a_list = [1, 2, 3, 2, 1]

    excepted = True
    actual = is_palidrome(a_list)

    assert excepted == actual


def test_is_palidrome_false():
    a_list = [1, 2, 3, 4, 2, 1]

    excepted = False
    actual = is_palidrome(a_list)

    assert excepted == actual