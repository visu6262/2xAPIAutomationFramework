# create a booking, Delete the booking with id and verify get request that id is exists or not

from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *
from src.helpers.codetest import *
import pytest
import json
import allure

class TestIntegrationTc2(object):

    @allure.title("Delete booking id using crud operations")
    @allure.description("Delete booking id")
    def test_delete_booking_id_integration(self,create_token, create_booking):
        responce = delete_request(url=Apiconstants().url_put_patch_delete(booking_id=create_booking),
                                  auth=None,
                                  headers=Utils().common_headars_put_patch_delete_cookie(token=create_token),
                                  in_json=False)
        print(create_booking)
        print(responce.text)
        verify_http_status(response_data=responce, expect_data=201)
        verify_resp_data_delete(resp_data=responce.text)

    def test_get_booking_id_integration(self,create_booking):
        responce = get_request(url=Apiconstants().url_put_patch_delete(booking_id=create_booking),
                               auth=None)

        try:
            print(responce.json())
        except AttributeError as e:
            print(e)
