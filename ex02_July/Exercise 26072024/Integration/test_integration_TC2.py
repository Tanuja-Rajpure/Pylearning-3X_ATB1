# Integration Scenario 2
#TC#2 Create Booking, Verify it and delete it

import allure
import requests
import pytest

@allure.title("Create Booking, Verify it and Delete It")
@allure.description("TC#2 Verify that booking can be deleted")
def test_delete_booking_byID(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com/"
    base_path= "/booking/"+ str(create_booking)
    booking_id = str(create_booking)
    DELETE_URL = base_url + base_path
    cookie = "token=" + create_token
    headers ={
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    response=requests.delete(url=DELETE_URL, headers=headers)
    print("Your deleted Id is: ", booking_id)

    # Verify if Id is deleted-> Get booking by ID
    get_response= requests.get(url=DELETE_URL)
    assert get_response.status_code == 404
