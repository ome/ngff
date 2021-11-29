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
    # To validate e.g. /examples/collection/valid/*.json the
    # schema_name will be 'collection'...
    schema_name = path.replace("examples/", "").split("/")[0]
    # ...so we can load the correct schema
    with open(f'schemas/json_schema/{schema_name}.schema') as f:
        schema = json.loads(f.read())

    with open(path) as f:
        test_json = json.loads(f.read())
    validate(instance=test_json, schema=schema)
