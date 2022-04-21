import json
import glob

import pytest

from jsonschema import RefResolver, Draft202012Validator
from jsonschema.exceptions import ValidationError


with open('schemas/bf2raw.schema') as f:
    bf2raw_schema = json.load(f)
with open('schemas/image.schema') as f:
    image_schema = json.load(f)
with open('schemas/strict_image.schema') as f:
    strict_image_schema = json.load(f)

schema_store = {
    bf2raw_schema['$id']: bf2raw_schema,
    image_schema['$id']: image_schema,
    strict_image_schema['$id']: strict_image_schema,
}

resolver = RefResolver.from_schema(image_schema, store=schema_store)
validator = Draft202012Validator(image_schema, resolver=resolver)
strict_validator = Draft202012Validator(strict_image_schema, resolver=resolver)
bf2raw_validator = Draft202012Validator(bf2raw_schema, resolver=resolver)

bf2raw_files = list(glob.glob("examples/bf2raw/*.json"))
valid_strict_files = list(glob.glob("examples/valid_strict/*.json"))
valid_files = list(glob.glob("examples/valid/*.json"))
invalid_files = list(glob.glob("examples/invalid/*.json"))
invalid_but_dont_fail_files = list(
    glob.glob("examples/invalid_but_dont_fail/*.json"))


def ids(files):
    return [str(x).split("/")[-1][0:-5] for x in files]


@pytest.mark.parametrize(
    "testfile", bf2raw_files, ids=ids(bf2raw_files))
def test_bf2raw(testfile):
    with open(testfile) as f:
        data = ''.join(line for line in f if not line.lstrip().startswith('//'))
        jsondata = json.loads(data)
        bf2raw_validator.validate(jsondata)


@pytest.mark.parametrize(
    "testfile", valid_strict_files, ids=ids(valid_strict_files))
def test_valid_strict(testfile):
    with open(testfile) as f:
        data = ''.join(line for line in f if not line.lstrip().startswith('//'))
        jsondata = json.loads(data)
        validator.validate(jsondata)
        strict_validator.validate(jsondata)


@pytest.mark.parametrize("testfile", valid_files, ids=ids(valid_files))
def test_valid_files(testfile):
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
        with pytest.raises(ValidationError):
            strict_validator.validate(json_file)


@pytest.mark.xfail
@pytest.mark.parametrize(
    "testfile", invalid_but_dont_fail_files,
    ids=ids(invalid_but_dont_fail_files))
def test_invalid_but_dontfail(testfile):
    with open(testfile) as f:
        json_file = json.load(f)
        with pytest.raises(ValidationError):
            validator.validate(json_file)
        with pytest.raises(ValidationError):
            strict_validator.validate(json_file)