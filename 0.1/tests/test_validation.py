import json
import os
import glob

import pytest

from jsonschema import validate
from jsonschema.validators import validator_for
from jsonschema.exceptions import ValidationError


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 8000)


def files():
    return list(glob.glob(f"examples/*/valid/*.json")) + \
        list(glob.glob(f"examples/*/invalid/*.json"))


def strict():
    return list(glob.glob(f"examples/image/valid/*.json"))


def ids(paths):
    return [str(x).split("/")[-1][0:-5] for x in paths]


@pytest.mark.parametrize("testfile", files(), ids=ids(files()))
def test_json(testfile):

    test_json, schema = load_instance_and_schema(testfile)

    if "invalid" in testfile:
        with pytest.raises(ValidationError):
            validate(instance=test_json, schema=schema)
    else:
        validate(instance=test_json, schema=schema)


@pytest.mark.parametrize("testfile", strict(), ids=ids(strict()))
def test_strict_rules(testfile, httpserver):

    for uri, filename in (
        ("/image.schema", "schemas/json_schema/image.schema"),
    ):
        with open(filename) as o:
            httpserver.expect_request(uri).respond_with_data(o.read())

    test_json, schema = load_instance_and_schema(testfile, strict=True)

    # Check for all validation errors without throwing exception
    cls = validator_for(schema)
    cls.check_schema(schema)
    validator = cls(schema)
    warnings = list(validator.iter_errors(test_json))
    for warning in warnings:
        print("WARNING", warning.message)
    # ONLY the complete example has no warnings in strict mode
    if "complete" not in testfile:
        assert len(warnings) > 0


def load_instance_and_schema(path, strict=False):
    # Load the correct schema
    test_json = load_json(path)
    # we don't have @type in this version
    if "multiscales" in test_json:
        schema_name = "image.schema"
    elif "plate" in test_json:
        schema_name = "plate.schema"
    else:
        raise Exception("No schema found")

    schema = load_json('schemas/json_schema/' + schema_name)

    strict_path = 'schemas/json_schema/strict_' + schema_name
    if strict and schema_name == "image.schema":
        schema = load_json(strict_path)
        # If the schema were using an external URL, could point at local image.schema
        # schema['allOf'][0]['$ref'] = "http://localhost:8000/image.schema"

    return (test_json, schema)


def load_json(path):
    with open(path) as f:
        json_data = json.loads(f.read())
    return json_data


def merge(destination, source):
    """
    deep merge of source into destination dict
    https://stackoverflow.com/questions/20656135/python-deep-merge-dictionary-data
    """
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            merge(node, value)
        else:
            destination[key] = value

    return destination