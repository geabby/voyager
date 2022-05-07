import requests
import os
import ujson
import base64
import time

def api_url():
    """
    returns api_url entered by the user during execution
    """
    return os.environ['API_URL']

def make_get_request(route, headers):
    """
    makes get request based on route and header values passed
    the method returns the code and the response body
    """
    try:
        resp_content = None
        print(route,headers)
        resp = requests.get(route, headers=headers)
        time.sleep(0.2)
        resp_content = resp.json()
        print(f"response {resp_content}")
    except Exception as exp:
        raise RuntimeError(f'Error: Response returned for make_get_request {route} with response ->: {resp_content}. \n Also check if env is up and running \n Exception {exp}')  # noqa: E501
    return resp.json(), resp.status_code

def make_post_request(route, headers, params={}):
    """
    makes post request based on route and header and optional params passed
    the method returns the code and the response body
    """
    try:
        resp_content = None
        resp = requests.post(route, headers=headers, **params)
        time.sleep(0.2)
        resp_content = resp.json()
    except Exception as exp:
        resp_content = resp.content
        raise RuntimeError(f'Error: Response returned for make_post_request {route} with response ->: {resp_content}. \n Also check if env is up and running \n Exception {exp}')  # noqa: E501
    return resp.json(), resp.status_code
