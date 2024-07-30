import allure
import pytest
import requests


@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To Make request we need
    # url-
    # Method - POST
    # header
    # Payload- Body- Dict / JSON
    # Auth - No
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "Tanu",
        "lastname": "Pure",
        "totalprice": 111,
        "depositpaid": True, # Just make this true to True
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload) # Positional Parameters
    assert response.status_code == 200

    responseData = response.json()

    # response Body Verification
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time response
    assert responseData["bookingid"] != None
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    assert firstname == "Tanu"
    assert lastname == "Pure"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


@allure.title("Create Booking CRUD")
@allure.description("TC#2 -Verify booking not created with {} data")
@pytest.mark.crud

def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type":"application/json"}
    json_payload = {

    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #assertion
    assert response.status_code == 500


@allure.title("Create Booking CRUD")
@allure.description("TC#3 - Verify booking total price is string" )
@pytest.mark.crud

def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type":"application/json"}
    json_payload = {
        "firstname": "Tanu",
        "lastname": "Pure",
        "totalprice": "tanuja",
        "depositpaid": True,  # Just make this true to True
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    responseData = response.json()
    totalprice = responseData["booking"]["totalprice"]

    #assertion
    assert response.status_code == 200