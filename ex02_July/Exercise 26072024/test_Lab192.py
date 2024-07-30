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


def test_update_request_1(create_token,create_booking_id):
    print("Token is-", create_token)
    print("Booking Id is- ", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Shital",
        "lastname": "Jadhav",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)

    assert response.status_code == 200
    responseData = response.json()
    print(responseData)
    assert responseData["firstname"] == "Shital"
def test_update_request_2(create_token,create_booking_id):
    print("Token is-", create_token)
    print("Booking Id is- ", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Shital",
        "lastname": "Jadhav",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)

    assert response.status_code == 200
    responseData = response.json()
    print(responseData)
    assert responseData["firstname"] == "Shital"