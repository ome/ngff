import os
import json
import glob

import pytest

from jsonschema import validate as js_valid
from jsonschema.exceptions import ValidationError as JSErr


def test_json(method, testfile):

    if "invalid" in testfile:
        with pytest.raises(JSErr):
            method(testfile)
    else:
        method(testfile)


def files():
    return list(glob.glob(f"examples/valid/*.json")) + \
        list(glob.glob(f"examples/invalid/*.json"))

def ids():
    return [str(x).split("/")[-1][0:-5] for x in files()]


@pytest.fixture(params=files(), ids=ids())
def testfile(request):
    return request.param


@pytest.fixture(params=("jsonschema",))
def method(request):

    with open('schemas/json_schema/collection.schema') as f:
        schema = json.loads(f.read())

    def json_schema(path):
        with open(path) as f:
            test_json = json.loads(f.read())
        return js_valid(instance=test_json, schema=schema)

    return json_schema

