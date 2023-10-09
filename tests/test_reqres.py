from allure_commons.types import Severity
from jsonschema.validators import validate
import allure
from conftest import api_requests, load_schema
from utils.models import base_url


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.description('Users list')
@allure.title('Checking the method to return a user list')
@allure.link(base_url, name='Testing')
def test_users_list():
    per_page = 6

    with allure.step(f'Create a GET request with parameter "per_page"'):
        response = api_requests(method="get",
                                url="/api/users",
                                params={"per_page": per_page}
                                )

    with allure.step(f'Checking the status code of users and data'):
        assert response.status_code == 200
        assert response.json()["per_page"] == per_page
        assert len(response.json()["data"]) == per_page


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.description('Users list')
@allure.title('Checking the method to return a user list by schema')
@allure.link(base_url, name='Testing')
def test_users_list_schema():
    schema = load_schema("get_list_users.json")
    with allure.step(f'Create a GET request with parameter "per_page"'):
        response = api_requests(method="get",
                                url="/api/users")
    with allure.step(f'Checking the data'):
        validate(instance=response.json(), schema=schema)


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Creation a new user')
@allure.title('Checking a creation a new user')
@allure.link(base_url, name='Testing')
def test_create_user():
    name = "Doja"
    job = "Cat"
    with allure.step(f'Create a POST request with valid data'):
        response = api_requests(method="post",
                                url="/api/users",
                                json={"name": name,
                                      "job": job}
                                )

    with allure.step(f'Checking the status code of users and data'):
        assert response.status_code == 201
        assert response.json()["name"] == name
        assert response.json()["job"] == job


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Creation a new user')
@allure.title('Checking a creation a new user')
@allure.link(base_url, name='Testing')
def test_create_user_schema():
    name = "Doja"
    job = "Cat"
    schema = load_schema("post_new_user.json")

    with allure.step(f'Create a POST request with valid data by schema'):
        response = api_requests(method="post",
                                url="/api/users",
                                json={"name": name,
                                      "job": job}
                                )

    with allure.step(f'Checking the data'):
        validate(instance=response.json(), schema=schema)


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.description('Update user')
@allure.title('Updating already created user')
@allure.link(base_url, name='Testing')
def test_update_user():
    name = "Amala Doja"
    job = "Cat"
    with allure.step(f'Create a PATCH request with valid data'):
        response = api_requests(method="patch",
                                url="/api/users/2",
                                json={"name": name,
                                      "job": job}
                                )

    with allure.step(f'Checking the status code of users and data'):
        assert response.status_code == 200
        assert response.json()["name"] == name
        assert response.json()["job"] == job


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.description('Update user')
@allure.title('Updating already created user by schema')
@allure.link(base_url, name='Testing')
def test_update_user_schema():
    name = "Amala Doja"
    job = "Cat"
    schema = load_schema("patch_user_data.json")

    with allure.step(f'Create a PATCH request with valid data by schema'):
        response = api_requests(method="patch",
                                url="/api/users/2",
                                json={"name": name,
                                      "job": job}
                                )

    with allure.step(f'Checking the data'):
        validate(instance=response.json(), schema=schema)


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Delete user')
@allure.title('Checking deletion of user')
@allure.link(base_url, name='Testing')
def test_delete_user():
    with allure.step(f'Create a DELETE request to delete a data'):
        response = api_requests(method="delete",
                                url="/api/users/2"
                                )

    with allure.step(f'Checking the status code "No information"'):
        assert response.status_code == 204


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Successful registration')
@allure.title('Checking the successful registration with valid data')
@allure.link(base_url, name='Testing')
def test_successful_registration():
    email = "eve.holt@reqres.in"
    password = "pistol"
    with allure.step(f'Create a POST request with valid data for successful registration'):
        response = api_requests(method="post",
                                url="/api/register",
                                json={"email": email,
                                      "password": password}
                                )

    with allure.step(f'Checking the status code and not empty token'):
        assert response.status_code == 200
        assert response.json()["token"] is not None


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Unsuccessful registration')
@allure.title('Checking the unsuccessful registration with invalid data')
@allure.link(base_url, name='Testing')
def test_unsuccessful_registration():
    email = "eve.holt@reqres.in"
    password = ""
    with allure.step(f'Create a POST request with invalid data for unsuccessful registration'):
        response = api_requests(method="post",
                                url="/api/register",
                                json={"email": email,
                                      "password": password}
                                )

    with allure.step(f'Checking the status code and the error "Missing password"'):
        assert response.status_code == 400
        assert response.json()["error"] == 'Missing password'


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Successful login')
@allure.title('Checking the successful login with valid data')
@allure.link(base_url, name='Testing')
def test_successful_login():
    email = "eve.holt@reqres.in"
    password = "cityslicka"
    with allure.step(f'Create a POST request with valid data for successful login'):
        response = api_requests(method="post",
                                url="/api/register",
                                json={"email": email,
                                      "password": password}
                                )

    with allure.step(f'Checking the status code and not empty token'):
        assert response.status_code == 200
        assert response.json()["token"] == "QpwL5tke4Pnpja7X4"


@allure.label('owner', 'Alexandra Borland')
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.description('Unsuccessful login')
@allure.title('Checking the unsuccessful login with invalid data')
@allure.link(base_url, name='Testing')
def test_unsuccessful_login():
    email = "eve.holt@reqres.in"
    password = ""
    with allure.step(f'Create a POST request with invalid data for unsuccessful login'):
        response = api_requests(method="post",
                                url="/api/register",
                                json={"email": email,
                                      "password": password}
                                )

    with allure.step(f'Checking the status code and the error "Missing password"'):
        assert response.status_code == 400
        assert response.json()["error"] == 'Missing password'
