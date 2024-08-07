# Python concept- Fixture
import pytest


# Use-
# Provide context to test case
# Similar to pre cont , post cond
# Pre conditions - token, booking id- Fixture
# test_update_negative_1
# test_update_positive_2

# Set up and Tear down - Pre and Post conditions



@pytest.fixture
def is_married():
    return True

def test_i_need_confirm(is_married):
    assert is_married == True
        