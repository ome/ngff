"""
This test evalutes all of the files under the examples/ directory
using the configuration in the provided config file in order detect
what should be run. It is assumed that all files are valid and complete
so that they can be wholly included into the specification.
"""
import json
import glob

import pytest

from jsonschema import RefResolver, Draft7Validator
from jsonschema.exceptions import ValidationError

def pytest_generate_tests(metafunc):
    if "suite" in metafunc.fixturenames:
        suites = []
        ids = []
        for config_filename in glob.glob("examples/*/.config.json"):
            with open(config_filename) as o:
                data = json.load(o)
            schema = data["schema"]
            for filename in glob.glob("examples/*/*.json"):
                ids.append(str(filename).split("/")[-1][0:-5])
                with open(filename) as f:
                    # Strip comments
                    data = ''.join(line for line in f if not line.lstrip().startswith('//'))
                    jsondata = json.loads(data)
                suites.append((schema, jsondata))
        metafunc.parametrize("suite", suites, ids=ids, indirect=True)


@pytest.fixture
def suite(request):
    return request.param

def test_run(suite):
    schema, jsondata = suite

    # Load schema
    with open(schema) as f:
        schema = json.load(f)
    schema_store = {
        schema['$id']: schema
    }
    resolver = RefResolver.from_schema(schema, store=schema_store)
    validator = Draft7Validator(schema, resolver=resolver)

    # Test loaded data
    validator.validate(jsondata)