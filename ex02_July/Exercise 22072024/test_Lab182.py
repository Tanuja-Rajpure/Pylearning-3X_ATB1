import pytest


@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@pytest.mark.regression
def test_sub1():
    assert 1 - 1 == 0


@pytest.mark.smoke
def test_sub2():
    assert 3 - 3 == 0


@pytest.mark.skip
def test_sub3():
    assert 0 - 4 == 0
