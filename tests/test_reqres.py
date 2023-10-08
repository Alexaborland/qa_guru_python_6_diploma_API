import json
import os

import requests
from jsonschema.validators import validate

from conftest import api_requests, load_schema


def test_users_list():
    per_page = 6

    response = api_requests(method="get",
                            url="/api/users",
                            params={"per_page": per_page}
                            )

    assert response.status_code == 200
    assert response.json()["per_page"] == per_page
    assert len(response.json()["data"]) == per_page


def test_users_list_schema():
    schema = load_schema("get_list_users.json")
    response = api_requests(method="get",
                            url="/api/users")
    validate(instance=response.json(), schema=schema)


def test_create_user():
    name = "Doja"
    job = "Cat"
    response = api_requests(method="post",
                            url="/api/users",
                            json={"name": name,
                                  "job": job}
                            )

    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_create_user_schema():
    name = "Doja"
    job = "Cat"
    schema = load_schema("post_new_user.json")

    response = api_requests(method="post",
                            url="/api/users",
                            json={"name": name,
                                  "job": job}
                            )

    validate(instance=response.json(), schema=schema)


def test_update_user():
    name = "Amala Doja"
    job = "Cat"
    response = api_requests(method="patch",
                            url="/api/users/2",
                            json={"name": name,
                                  "job": job}
                            )

    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_update_user_schema():
    name = "Amala Doja"
    job = "Cat"
    schema = load_schema("patch_user_data.json")

    response = api_requests(method="patch",
                            url="/api/users/2",
                            json={"name": name,
                                  "job": job}
                            )

    validate(instance=response.json(), schema=schema)


def test_delete_user():
    response = api_requests(method="delete",
                            url="/api/users/2"
                            )

    assert response.status_code == 204


def test_successful_registration():
    email = "eve.holt@reqres.in"
    password = "pistol"
    response = api_requests(method="post",
                            url="/api/register",
                            json={"email": email,
                                  "password": password}
                            )

    assert response.status_code == 200
    assert response.json()["token"] is not None


def test_unsuccessful_registration():
    email = "eve.holt@reqres.in"
    password = ""
    response = api_requests(method="post",
                            url="/api/register",
                            json={"email": email,
                                  "password": password}
                            )

    assert response.status_code == 400
    assert response.json()["error"] == 'Missing password'


def test_successful_login():
    email = "eve.holt@reqres.in"
    password = "cityslicka"
    response = api_requests(method="post",
                            url="/api/register",
                            json={"email": email,
                                  "password": password}
                            )

    assert response.status_code == 200
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"


def test_unsuccessful():
    email = "eve.holt@reqres.in"
    password = ""
    response = api_requests(method="post",
                            url="/api/register",
                            json={"email": email,
                                  "password": password}
                            )

    assert response.status_code == 400
    assert response.json()["error"] == 'Missing password'