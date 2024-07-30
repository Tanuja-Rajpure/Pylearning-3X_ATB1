import pytest
import requests
import allure
@pytest.fixture()
def create_token():
    print("Creating Token...")
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    token = response.json()["token"]
    print("Your Token is-", token)
    return token
@pytest.fixture()
def create_booking_id():
    print("Creating Booking ID...")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Jadhav",
        "totalprice": 111,
        "depositpaid": True,  # Just make this true to True
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    # assertion
    assert response.status_code == 200

    responseData = response.json()
    booking_id = responseData["bookingid"]
    print("Your Booking Id is-", booking_id)
    return booking_id
@pytest.fixture()
def launch_browser():
    print("Launching Browser !! Chrome")
    return "Chrome"
@pytest.fixture()
def close_browser():
    print("Closing browser !! Chrome")
    return "Closed"
