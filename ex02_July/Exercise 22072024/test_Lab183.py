import allure
import pytest


@allure.title("TC#1 - Verity that 2-2 equal to zero")
@allure.description("This is a smoke test case, which check 2-2 equal to zero")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@allure.title("TC#2 - Verity that 1-1 equal to zero")
@allure.description("This is a smoke test case, which check 1-1 equal to zero")
@pytest.mark.regression
def test_sub1():
    assert 1 - 1 == 0


@allure.title("TC#3 - Verity that 3-3 equal to zero")
@allure.description("This is a smoke test case, which check 3-3 equal to zero")
@pytest.mark.smoke
def test_sub2():
    assert 3 - 3 == 0


@allure.title("TC#4 - Verity that 0-4 is not equal to zero")
@allure.description("This is a smoke test case, which check 0-4 is not equal to zero")
@pytest.mark.skip
def test_sub3():
    assert 0 - 4 == 0
