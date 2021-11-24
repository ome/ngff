import os
import json
import glob

import pytest

from jsonschema import validate as js_valid
from jsonschema.exceptions import ValidationError as JSErr

from pyld import jsonld
from pyshacl import validate as ld_valid
from rdflib import Graph

from schema_salad.schema import load_schema, load_and_validate
from schema_salad.exceptions import ValidationException as SaladErr


# NB: Need to have contents of /json_schema served at localhost:8000
# so that http://localhost:8000/omero.schema.json is valid

# cd json_schema
# python -m http.server

# class LDErr(Exception):
#     pass


def test_json(method, testfile):
    if "invalid" in testfile:
        with pytest.raises((JSErr)):
            method(testfile)
    else:
        method(testfile)


def files():
    return list(glob.glob(f"examples/collections/valid/*.json")) + \
        list(glob.glob(f"examples/collections/invalid/*.json"))

def ids():
    return [str(x).split("/")[-1][0:-5] for x in files()]


@pytest.fixture(params=files(), ids=ids())
def testfile(request):
    return request.param


@pytest.fixture(params=("jsonschema",))
def method(request):

    # if request.param == "jsonschema":

    with open('json_schema/collection.schema') as f:
        schema = json.loads(f.read())

    def f(path):
        with open(path) as f:
            test_json = json.loads(f.read())
        return js_valid(instance=test_json, schema=schema)

    return f
