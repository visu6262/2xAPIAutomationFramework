import json

from src.constants.api_constants import *
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

import pytest
import allure
import openpyxl

def read_credentials_from_xlsx(file_name_or_path):
    credentials=[]
    wb=openpyxl.load_workbook(filename=file_name_or_path)
    sheet=wb.active
    for r in sheet.iter_rows(min_row=2,values_only=True):
        a,b = r
        credentials.append(({"username":a,"password":b}))
        # print("printing 1",credentials)
    return credentials


def create_auth_request(username,password):
    payload={
    "username" : username,
    "password" : password
    }

    respsonce =post_request(url=Apiconstants().url_create_token(),
                           headers=Utils().common_headars_json(),
                           auth=None,
                           payload=payload,
                           in_json=False)
    return respsonce

@pytest.mark.parametrize("uidpwd",read_credentials_from_xlsx(file_name_or_path=r"C:\Users\91939\PycharmProjects\2xAPIAutomationFramework\tests\test\datadriventesting\testdata.xlsx"))
def test_create_auth_from_xlsx(uidpwd):
    username =uidpwd["username"]
    password = uidpwd["password"]
    resp=create_auth_request(username=username,password=password)
    print("Status code is ==>",resp.status_code)