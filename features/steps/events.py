import logging
import json
import os
from time import sleep
from user import User

@then('the listing response should have field')
def check_num_field_value(test_context):
    response = test_context.response_body
    for row in test_context.table:
        field_name = row['field_name']
        for record in response:
            result = record[field_name]
            assert result is not None, f'Error: Field {field_name} should exist but does'


@then('the events response should have "{num:d}" results')
def check_num_field_value(test_context,num):
    response = test_context.response_body
    assert len(response) is num, f'Error: Num of results is not {num}'




