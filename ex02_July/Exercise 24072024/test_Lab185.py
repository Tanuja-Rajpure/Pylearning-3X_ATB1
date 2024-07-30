import allure
import pytest
import requests


@allure.title("Test GET Request - Restful Booker project #1")
@allure.description("TC#5 - Verify that GET request wih ID works")
@allure.tag("smoke", "po")
@allure.label("Owner", "Tanuja Rajpure")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_idt():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200