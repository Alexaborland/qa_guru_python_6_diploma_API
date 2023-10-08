import os
import json
import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def load_schema(name: str):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'schema', name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


def api_requests(method, url, **kwargs):
    base_url = "https://reqres.in"
    new_url = base_url + url
    method = method.upper()
    with allure.step(f"{method} {url}"):
        with sessions.Session() as session:
            response = session.request(method=method,
                                       url=new_url,
                                       **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode("utf8"),
                          name="Curl",
                          attachment_type=AttachmentType.TEXT,
                          extension="txt")
            if not response.content:
                allure.attach(body=message.encode("utf8"),
                              name="Text",
                              attachment_type=AttachmentType.TEXT)
            else:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"),
                              name="Response Json",
                              attachment_type=AttachmentType.JSON,
                              extension="json")
    return response





