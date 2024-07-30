# Request Module-
# Package or library contains functions which you can use easily
# Modules - math, os, allure, pytest

# Tomake diff request HTTP - methods
# Request - module
# GET , POST, PUT, PATCH, DELETE , OPTIONS .... HTTPS Methods
# It support URL, AUTH, Cookies , Verification with pytest.

# GET Request to Booking ID
# WHat need =
# URL = https://restful-booker.herokuapp.com/booking
# AUTH = No
# Payload = No
# Header = No
# Query Param = No
# Path Param - Yes- Booking ID

# Response
# Body- Verify- Assert., Keys- value
# Status code- verify
# Time
# JSON Schema
####################################

import allure
import pytest
import requests


@allure.title("Test GET Request - Restful Booker project #1")
@allure.description("TC#1 - Verify that GET request wih ID works")
@allure.tag("smoke", "po")
@allure.label("Owner", "Tanuja Rajpure")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200

@allure.title("Test GET Request - Restful Booker project #1")
@allure.description("TC#2 - Verify that GET request with invalid booking Id")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404

@allure.title("Test GET Request - Restful Booker project #1")
@allure.description("TC#3 - Verify that GET request with invalid status code")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404