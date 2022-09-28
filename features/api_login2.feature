Feature: API Login Testing 2


    Scenario: Login Testing 2
        Given   ReqRes Endpoint URL
        AND     Request Body
        When    Hit the login endpoint with given payload
        Then    Successful login

    @smoke
    Scenario: Login Unsuccessful 2
        Given   ReqRes Endpoint URL
        AND     Request Body Unsuccessful
        When    Hit the login endpoint with given payload
        Then    Successful login