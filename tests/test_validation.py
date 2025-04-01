import json
import glob

import pytest

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def files():
    return list(glob.glob(f"examples/*/valid/*.json")) + \
        list(glob.glob(f"examples/*/invalid/*.json"))

def ids():
    return [str(x).split("/")[-1][0:-5] for x in files()]


@pytest.mark.parametrize("testfile", files(), ids=ids())
def test_json(testfile):

    if "invalid" in testfile:
        with pytest.raises(ValidationError):
            json_schema(testfile)
    else:
        json_schema(testfile)


def json_schema(path):
    # Load the correct schema
    with open(path) as f:
        test_json = json.loads(f.read())
        # we don't have @type in this version
        if "multiscales" in test_json:
            schema_name = "image.schema"
        elif "plate" in test_json:
            schema_name = "plate.schema"
        elif "well" in test_json:
            schema_name = "well.schema"
        else:
            raise Exception("No schema found")

    with open('schemas/' + schema_name) as f:
        schema = json.loads(f.read())
    validate(instance=test_json, schema=schema)
