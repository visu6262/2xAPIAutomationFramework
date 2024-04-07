from src.constants.api_constants import *
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

import pytest
import allure


@pytest.fixture
def create_token():
    respsonce = post_request(url=Apiconstants().url_create_token(),
                             headers=Utils().common_headars_json(),
                             auth=None,
                             payload=payload_create_token(),
                             in_json=False)

    verify_http_status(response_data=respsonce, expect_data=200)
    token = respsonce.json()["token"]
    return token


@pytest.fixture()
def create_booking():
    responce = post_request(url=Apiconstants().url_create_booking(),
                            headers=Utils().common_headars_json(),
                            auth=None,
                            payload=payload_created_booking(),
                            in_json=False)
    verify_http_status(response_data=responce, expect_data=200)
    bookingid = responce.json()["bookingid"]
    return bookingid
