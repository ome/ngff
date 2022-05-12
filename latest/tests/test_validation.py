"""
This test consumes https://github.com/json-schema-org/JSON-Schema-Test-Suite#structure-of-a-test
styled JSON tests.
"""
import json
import glob

import pytest

from jsonschema import RefResolver, Draft7Validator
from jsonschema.exceptions import ValidationError


def pytest_generate_tests(metafunc):
    if "suite" in metafunc.fixturenames:
        suites = []
        for filename in glob.glob("tests/*.json"):
            with open(filename) as o:
                data = json.load(o)
            schema = data["schema"]
            for test in data["tests"]:
                suites.append((schema, test))
        metafunc.parametrize("suite", suites, indirect=True)


@pytest.fixture
def suite(request):
    return request.param


def test_run(suite):
    schema, test = suite

    # Load schema
    # Currently missing the "id" field
    with open(schema["id"]) as f:
        schema = json.load(f)
    schema_store = {
        schema['$id']: schema
    }
    resolver = RefResolver.from_schema(schema, store=schema_store)
    validator = Draft7Validator(schema, resolver=resolver)

    # Load data and test
    jsondata = test["data"]
    valid = test["valid"]
    if not valid:
        with pytest.raises(ValidationError):
            validator.validate(jsondata)