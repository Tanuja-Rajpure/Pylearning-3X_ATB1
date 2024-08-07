#Integration Scenarios
# 3) GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated

import allure
import pytest
import requests

@allure.title("GET an existing booking from GET all bookingid's")
@allure.description("TC#3 GET an existing booking from GET all bookingid's , "
                    "Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration

def test_get_update_verify_all_bookings_id(create_token):
    base_url = "https://restful-booker.herokuapp.com/booking/"


    #Step 1- Get all bookings

    get_url = base_url
    response = requests.get(url=get_url)
    assert response.status_code == 200
    all_bookings = response.json()

    #Ensure list is not empty
    assert len(all_bookings) != 0
    #print(all_bookings)

    #Get 1st booking Id
    bookingid = all_bookings[0]["bookingid"]
    print("First booking ID is:", bookingid)

    #Verify detils of 1st Id
    id_url = base_url + str(bookingid)
    response = requests.get(url=id_url)
    id_data = response.json()
    print("Your first Id Booking details are-", id_data)

    # Step 2- Update 1st booking
    update_url = base_url + str(bookingid)
    cookie = "token=" + create_token
    headers= {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    update_payload = {
        "firstname": "UpdateF",
        "lastname": "UpdateL",
        "bookingdates": {
            "checkin": "2018-02-10",
            "checkout": "2019-02-10"
        }
    }
    update_response = requests.patch(url=update_url, headers=headers, json=update_payload)
    assert update_response .status_code == 200

    # Step 3- Verify the update
    verify_response = requests.get(url=update_url)
    update_data = verify_response.json()
    assert update_data["firstname"] == "UpdateF"
    assert update_data["lastname"] == "UpdateL"
    assert update_data["bookingdates"]["checkin"] == "2018-02-10"
    assert update_data["bookingdates"]["checkout"] == "2019-02-10"
    print("Your first Id updated details are-", update_data)

