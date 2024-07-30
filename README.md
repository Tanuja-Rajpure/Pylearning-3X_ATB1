### How to Work wit Pytest

-pip install pytest
-File name - test_name.py
-Test name - test_nameOfTest():
-Assert - Actual Result == Expected Result

### How to run the pytest 
-open cmd - go to folder -pytest
-run directly from run icon

### PyTest Commands
-pytest -h
-To run all the test cased
  -pytest

-To run specific test case
    - We have to specify properly where is the path- 
    - Select file- right click - copy path refereance - content roof-
    - ex02_July/Exercise 22072024/test_Lab181.py
-
-To run specific test case with file
    - pytest -k "18"  -> It will run all test cases having 18 in name

-To run specific marked test case
- import pytest
- Add a annotation @pytest.mark.regression
- pytest -m "regression" "ex02_July/Exercise 22072024/test_Lab182.py"


### How to see the report of PyTest Test cases?
- Make sure that allure commandline is installed
- Download the node js
- If already installed check version-> node -v
- npm install -g npm allure commandline
- Verify that allure -> options
- Run Pytest test case- pytest "ex02_July/Exercise 22072024/test_Lab183.py" --alluredir=allure_result
- allure serve allure_result/
- to check result on cmd use '-s' ->
- pytest "ex02_July/Exercise 22072024/test_Lab183.py" --alluredir=allure_result -s