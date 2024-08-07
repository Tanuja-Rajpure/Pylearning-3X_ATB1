# 6) Trying to Update on a deleted id

import pytest
import allure
import requests


def test_delete_booking(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    booking_id = str(create_booking)
    print("booking_id to be delete is:", booking_id)
    DELETE_URL = base_url + base_path
    print(DELETE_URL)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    print("Your deleted booking Id is", str(create_booking))

    # Verify Id id deleted
    get_url= DELETE_URL
    get_response = requests.get(url=get_url)
    #response= get_response.json()
    assert get_response.status_code == 404

