import allure
import pytest
import requests
@allure.title("Create Token")
@pytest.fixture()
def create_token():
    print("Creating a Token")
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    responseData = requests.post(url=URL, headers=headers, json=json_payload)
    token = responseData.json()["token"]
    print("Your Token is-", token)
    return token

@pytest.fixture()
@allure.title("Create new Booking")
def create_booking():
    print("Creating a booking")
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {
        "Content_Type": "application/json"
    }
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    responseData = requests.post(url=URL, headers=headers, json=json_payload)
    assert responseData.status_code == 200

    response = responseData.json()
    Booking_id = response["bookingid"]
    print("Your Booking Id is", Booking_id)
    firstname = response["booking"]["firstname"]
    lastname = response["booking"]["lastname"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    print("Your Booking details are", response)
    return Booking_id
