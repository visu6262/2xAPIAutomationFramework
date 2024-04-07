# get an existing booking id from get all booking ids, update a booking and verify that updated bookingid


from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *
from src.helpers.codetest import *
import pytest
import json
import allure


class TestIntegrationTc3(object):

    def create_token(self):
        respsonce = post_request(url=Apiconstants().url_create_token(),
                                 headers=Utils().common_headars_json(),
                                 auth=None,
                                 payload=payload_create_token(),
                                 in_json=False)

        verify_http_status(response_data=respsonce, expect_data=200)
        token = respsonce.json()["token"]
        return token




    def test_get_booking_id_integration(self):
        responce = get_request(url=Apiconstants().url_create_booking(),
                               auth=None)

        verify_http_status(response_data=responce, expect_data=200)
        print(responce.json()[2])
        return responce.json()[2]

    def test_update_patch_interation(self):
        bookid = self.test_get_booking_id_integration()
        totok=self.create_token()
        resp = patch_request(url=Apiconstants().url_put_patch_delete(booking_id=bookid),
                             headers=Utils().common_headars_put_patch_delete_cookie(token=totok),
                             payload=payload_patch_partial_update_booking(),
                             auth=None,
                             in_json=True)

        # data = resp.json()
        print(resp)
        # verify_http_status(response_data=resp, expect_data=200)
        # assert resp.ok is True
        # verify_resp_key_value_checking(keyname=resp.json()["firstname"], expected_value="visu_visu")
        # verify_resp_key_value_checking(keyname=resp.json()["lastname"], expected_value="hyd")
