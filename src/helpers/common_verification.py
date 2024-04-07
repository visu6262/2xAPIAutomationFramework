import requests


def verify_http_status(response_data, expect_data):
    assert response_data.status_code == expect_data, "Status code not match"


def verify_json_key_not_null(key):
    assert key != 0, "Key is empty value" + key
    assert key > 0, "Key value is less then zero value"


def verify_json_key_not_none(key):
    assert key is not None, "Key value is not None"


def verify_resp_data_delete(resp_data):
    assert "Created" in resp_data


def verify_resp_key_value_checking(keyname,expected_value):
    assert keyname == expected_value