import pytest
@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_bookingid():
    return 123


def test_update_request_1(create_token,create_bookingid):
    print("Token is-", create_token)
    print("Booking Id is- ", create_bookingid)

def test_update_request_2(create_token,create_bookingid):
    print("Token is-", create_token)
    print("Booking Id is- ", create_bookingid)