# Veriry that create booking -> patch retuest - verify taht fisrtname updated or not

from conftest import *


class TestIntegrationCreateBookingPatch(object):

    # def test_create_booking_interation(self):
    #     resp = post_request(url=Apiconstants().url_create_booking(),
    #                        headers=Utils().common_headars_json(),
    #                        auth=None,
    #                        payload=payload_created_booking(),
    #                        in_json=False)
    #
    #     print(resp.json())
    #     booking_id = resp.json()["bookingid"]
    #     verify_http_status(response_data=resp, expect_data=200)
    #     verify_json_key_not_none(booking_id)
    #     verify_json_key_not_null(booking_id)
    #     verify_resp_key_value_checking(keyname=resp.json()["booking"]["firstname"], expected_value="Jim")
    #     print(resp.json()["booking"]["firstname"])
    #     return booking_id

    def test_update_patch_interation(self,create_booking,create_token):

        resp=patch_request(url=Apiconstants().url_put_patch_delete(booking_id=create_booking),
                           headers=Utils().common_headars_put_patch_delete_cookie(token=create_token),
                           payload=payload_patch_partial_update_booking(),
                           auth=None,
                           in_json=False)

        verify_http_status(response_data=resp, expect_data=200)
        assert resp.ok is True
        verify_resp_key_value_checking(keyname=resp.json()["firstname"], expected_value="visu_visu")
        verify_resp_key_value_checking(keyname=resp.json()["lastname"], expected_value="hyd")