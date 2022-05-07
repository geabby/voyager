Feature: Events API
    @prod
    Scenario: Test for events 200 success response
        Given I am a valid api user
        When I make a get request "events"
        Then the API should respond with status code "200"

    @prod
    Scenario: Test for events 200 success response with per_page param
        Given I am a valid api user
        When I make a get request "events?per_page=4"
        Then the API should respond with status code "200"
        And the events response should have "4" results

    @prod
    Scenario: Test for events fields to have non null value
            Given I am a valid api user
            When I make a get request "events"
            Then the API should respond with status code "200"
            And the listing response should have field
                |field_name|
                |id|
                |type|
                |actor|
                |repo|




#more fields can be added
#we can also add a check for the value as well




#tests
# We can add all tests which are defined in the api contract to ensure the contract is always adhered to
    # Scenario: Test for 304 Not modified case
    # Scenario: Test for 403 forbidden
    # Scenario: 500 Internal Server Error
    # Test different Query Parameters
     #-page
     #-per_page


#Note: I have not defined any test which tests the data at this level.
# Data could be subject to change which could make the test flaky
# based on our confidence in data we can either add a test here or at the data level or mock the test to check how upstream systems handle the api based on certain data

#Note: I have not added all the tests we need to automated but focussed on the framework which can be expanded to add many different use cases
