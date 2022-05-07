import logging
import json
import os
from time import sleep
from user import User
from common_functions import (
    make_get_request,
    api_url
)

@given("I am a valid api user")
def step_api_token(test_context):
    test_context.user = User()
    test_context.api_url = api_url()

@then('the API should respond with status code "{code:d}"')
def check_status_code(test_context, code):
    assert test_context.response_status == code, f'Error: Code is not {code} received {test_context.response_status} with body {test_context.response_body} '  # noqa: E501

@then('the response body should have "{msg}" error message')
def check_num_field_value(test_context, msg):
    print(f"RESPONSE BODY {test_context.response_body}")
    response_value = search_hash(test_context.response_body, "error_message")
    print(f"RESPONSE VALUE {response_value}")
    assert str(
        response_value) == msg, f'Error: Json response {test_context.response_body} does not contain {value}'

# Note: ensure feature has url without a leading /
@when('I make a get request "{endpoint}"')
def get_request(test_context, endpoint):
    route = f"{test_context.api_url}/{endpoint}"
    headers = test_context.user.get_headers()
    resp_body, resp_status = make_get_request(route, headers)
    test_context.response_body = resp_body
    test_context.response_status = resp_status


@when('I make a post request "{endpoint}"')
def search_summary(test_context, endpoint):
    body = json.loads(test_context.text)
    route = f"{test_context.api_url}/{endpoint}"
    params = {
        'json': body
    }
    headers = test_context.user.post_headers
    resp_body, resp_status = make_post_request(route, headers, params)
    test_context.response_body = resp_body
    test_context.response_status = resp_status



