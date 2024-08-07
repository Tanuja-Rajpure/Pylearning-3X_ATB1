# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
import allure
import pytest
import requests

#Check health - If API working
@allure.title("Health Check")
@allure.description("TC#1 Verify API is working")
@pytest.mark.curd
def test_health_check():
    URL = "https://restful-booker.herokuapp.com/ping"

    responseData = requests.get(url=URL)
    assert responseData.status_code == 201
    print("API is working")

#Update fist name and last name with PATCH request
@allure.title("Partial update = Patch test")
@allure.description("TC#2 Test that partial update working with PATCH for first name and Last name")
#@pytest.mark.integration
def test_update_name_with_patch(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    #booking_id = str(create_booking)
    PATCH_URL = base_url + base_path
    print("PATCH URL IS:", PATCH_URL)
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie,
    }
    patch_payload = {
        "firstname": "John",
        "lastname": "BrownE",
    }

    patch_response = requests.patch(url=PATCH_URL, headers=headers, json=patch_payload)
    assert patch_response.status_code == 200
    patched_data = patch_response.json()
    # assert patched_data["firstname"] == "John"
    # assert patched_data["lastname"] == "BrownE"
    # print(f'Patched booking data is:{patched_data}')

    # Verify first name is updated
    get_response = requests.get(url=PATCH_URL)
    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data["firstname"] == "John"
    assert patched_data["lastname"] == "BrownE"
    print(f"Verified Patched Booking Data: {get_data}")
