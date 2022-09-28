Feature: API Login Testing

    @sanity
    Scenario: Login Testing
        Given   ReqRes Endpoint URL
        AND     Request Body
        When    Hit the login endpoint with given payload
        Then    Successful login

    @smoke
    Scenario: Login Unsuccessful
        Given   ReqRes Endpoint URL
        AND     Request Body Unsuccessful
        When    Hit the login endpoint with given payload
        Then    Successful login