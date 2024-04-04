
class Apiconstants(object):

    @staticmethod
    def url_base():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"


    def url_put_patch_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)