# PUT request
# Pre conditions:-
#Path- Booking ID exist
# URL
# Auth - Token
# Payload
import requests
import allure
import pytest
def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    token = response.json()["token"]
    print("Your Token is-", token)
    return token



def create_booking():
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
    print(responseData)
    return booking_id



def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+ str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token()
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
    print("Your data after updating first name:,", responseData)
    assert responseData["firstname"] == "Shital"


###############################################
def test_patch_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PATCH_URL = base_url + base_path
    cookie = "token+" + create_token()
    headers = {
        "content_Type": "application/json",
        "cookie": cookie
    }
    patch_payload = {
        "firstname": "Jenny"
    }

    patch_response = requests.patch(url=PATCH_URL, headers=headers, json=patch_payload)
    assert patch_response.status_code == 200
    patched_data = patch_response.json()

    #Verify patched update
    #get_url = PATCH_URL
    getpatched_response = requests.get(url=PATCH_URL, headers=headers)
    get_response= getpatched_response.json()
    assert get_response["firstname"] == "Jenny"
    print(("Your patched dats is:", get_response))
    assert get_response.status_code == 200








###############################################
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()

    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)
    print("Your deleted booking Id is", booking_id)

