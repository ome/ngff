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
validator = Draft202012Validator(image_schema, resolver=resolver)
strict_validator = Draft202012Validator(strict_image_schema, resolver=resolver)

valid_files = list(glob.glob("examples/valid/*.json"))
invalid_files = list(glob.glob("examples/invalid/*.json"))
valid_not_strict_files = list(glob.glob("examples/valid_if_not_strict/*.json"))


def ids(files):
    return [str(x).split("/")[-1][0:-5] for x in files]


@pytest.mark.parametrize("testfile", valid_files, ids=ids(valid_files))
def test_valid(testfile):
    with open(testfile) as f:
        json_file = json.load(f)
        validator.validate(json_file)
        strict_validator.validate(json_file)


@pytest.mark.parametrize(
    "testfile", valid_not_strict_files, ids=ids(valid_not_strict_files))
def test_valid_not_strict_files(testfile):
    with open(testfile) as f:
        json_file = json.load(f)
        validator.validate(json_file)
        with pytest.raises(ValidationError):
            strict_validator.validate(json_file)


@pytest.mark.parametrize("testfile", invalid_files, ids=ids(invalid_files))
def test_invalid(testfile):
    with open(testfile) as f:
        json_file = json.load(f)
        with pytest.raises(ValidationError):
            validator.validate(json_file)
