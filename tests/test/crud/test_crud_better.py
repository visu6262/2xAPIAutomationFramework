from src.constants.api_constants import *
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

import pytest
import allure


class TestCrudBooking(object):

    @allure.title("Update booking id using crud operations")
    @allure.description("Update booking id")
    def test_crud_update_booking_id(self, create_token, create_booking):
        responce = put_request(url=Apiconstants().url_put_patch_delete(booking_id=create_booking),
                               headers=Utils().common_headars_put_patch_delete_cookie(token=create_token),
                               auth=None,
                               payload=payload_update_booking(),
                               in_json=False)
        print(responce.json())
        verify_http_status(response_data=responce, expect_data=200)

    @allure.title("Delete booking id using crud operations")
    @allure.description("Delete booking id")
    def test_crud_delete_booking_id(self, create_token, create_booking):
        responce = delete_request(url=Apiconstants().url_put_patch_delete(booking_id=create_booking),
                                  auth=None,
                                  headers=Utils().common_headars_put_patch_delete_cookie(token=create_token),
                                  in_json=False)
        print(responce.text)
        verify_http_status(response_data=responce, expect_data=201)
        verify_resp_data_delete(resp_data=responce.text)
