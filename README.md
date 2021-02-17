# COUNTRY COVID TEST ACTIVITY API REST
API REST which allows to request the testing results made during COVID pandemic by country and date. 

## 1º STEP: Create Connection.
* Open a command console in the main directory and execute the connection script using: python connection.py

    This will create an open host (http://127.0.0.1:5000/) which will be used to make the requests. 

## 2º STEP: Test the API REST. 
There are two ways to test the API REST: 
1. Execute the test in the main folder using: python test.py
2. Using a service as POSTMAN to make requests. In this case it is necessary to:

    * Open the service and introduce the host (http://127.0.0.1:5000/) in the host bar. Followed by:
        * country_tests_done: If the JSON request contains country information.
        * date_tests_done: If the JSON request contains date information.
    * Select GET method.
    * In the body section introduce as JSON the information to filter. Example:
    
        {"country": "ES"}
        or 
        {"date": "2020-12"}
    
    