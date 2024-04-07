import json

from src.constants.api_constants import Apiconstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_created_booking
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_http_status, verify_json_key_not_none, verify_json_key_not_null

import pytest
import allure
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError

class TestCreateBookingJsonSchema(object):

    def load_schema(self,file_name):
        with open(file_name,"r") as file:
            return json.load(file)


    @allure.title("create booking")
    @allure.description("Create booking with +ve test")
    # @pytest.mark.smoke
    def test_create_booking(self):
        response = post_request(url=Apiconstants().url_create_booking(),
                                 auth=None,
                                 headers=Utils().common_headars_json(),
                                 payload=payload_created_booking(),
                                 in_json=False)

        Booking_id = response.json()["bookingid"]
        verify_http_status(response_data=response,expect_data=200)
        verify_json_key_not_none(Booking_id)
        verify_json_key_not_null(Booking_id)
        assert response.status_code == 200
        assert response.ok is True

        file_path=(r"C:\Users\91939\PycharmProjects\2xAPIAutomationFramework\tests\test\crud\create_booking_json_schema.json")
        schema=self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(),schema=schema)
        except ValidationError as e:
            print(e.message)
