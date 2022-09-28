from behave import *
from Helper.CRUD import CRUD
from Utilities.ConfigParse import ReadProperties

def base_url(context, section,key):
    context.base_url = ReadProperties.read_configuration(section,key)



@given(u'ReqRes Endpoint URL')
def endpoint_url(context):
    context.endpoint_url = "https://reqres.in/api/login"


@given(u'Request Body')
def request_body(context):
    context.payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

@given(u'Request Body Unsuccessful')
def request_body(context):
    context.payload = {
    "email": "eve.holt@reqres.in"
    }

@when(u'Hit the login endpoint with given payload')
def submitting_login(context):
    resp = CRUD.post_method(context.endpoint_url, context.payload)
    CRUD.validate_status_code(resp, 200)
    CRUD.validate_response(resp,"token", "QpwL5tke4Pnpja7X4")


@then(u'Successful login')
def check_login(context):
    pass
