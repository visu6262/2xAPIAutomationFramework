
class Utils(object):

    def common_headars_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headars_xml(self):
        headers = {
            "Content-Type": "text/xml"
        }
        return headers

    # Cookie: token=abc123

    def common_headars_put_patch_delete_cookie(self,token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token =" + str(token),
        }
        return headers

    def common_headars_put_patch_delete_basic_auth(self,basic_auth):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + str(basic_auth),
        }
        return headers