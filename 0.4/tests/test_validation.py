import json
import glob

import pytest

from jsonschema import RefResolver, Draft202012Validator
from jsonschema.exceptions import ValidationError


with open('schemas/image.schema') as f:
    image_schema = json.load(f)
with open('schemas/strict_image.schema') as f:
    strict_image_schema = json.load(f)
schema_store = {
    image_schema['$id']: image_schema,
    strict_image_schema['$id']: strict_image_schema,
}

resolver = RefResolver.from_schema(image_schema, store=schema_store)

# Dictionary of validators
validators = {}
strict_validators = {}
validators["multiscales"] = Draft202012Validator(
    image_schema, resolver=resolver)
strict_validators["multiscales"] = Draft202012Validator(
    strict_image_schema, resolver=resolver)


json_files = list(glob.glob("examples/**/*.json"))


def ids(files):
    return [str(x).split("/")[-1][0:-5] for x in files]

def get_spec(jsondata):
    for s in ["multiscales"]:
        if s in jsondata.keys():
            return s
    raise Exception("No specification found %s" % jsondata.keys())


@pytest.mark.parametrize("json_file", json_files, ids=ids(json_files))
def test_compliance(json_file):
    with open(json_file) as f:
        data = ''.join(line for line in f if not line.lstrip().startswith('//'))
        jsondata = json.loads(data)

    spec = get_spec(jsondata)
    if jsondata.get("valid", True):
        validators[spec].validate(jsondata)
    else:
        with pytest.raises(ValidationError):
            validators[spec].validate(jsondata)

    if jsondata.get("recommended", True) and jsondata.get("valid", True):
        strict_validators[spec].validate(jsondata)
    else:
        with pytest.raises(ValidationError):
            strict_validators[spec].validate(jsondata)
