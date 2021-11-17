
import os
import json

import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# NB: Need to have contents of /json_schema served at localhost:8000
# so that http://localhost:8000/omero.schema.json is valid

# cd json_schema
# python -m http.server

with open('json_schema/image.schema') as f:
  schema = json.loads(f.read())


# Test valid files
invalid_paths = [entry.path for entry in os.scandir("examples/valid")]
@pytest.mark.parametrize("path", invalid_paths)
def test_valid(path):
  with open(path) as f:
    test_json = json.loads(f.read())
    validate(instance=test_json, schema=schema)


# Test invalid files
invalid_paths = [entry.path for entry in os.scandir("examples/invalid")]
@pytest.mark.parametrize("path", invalid_paths)
def test_invalid(path):
  with open(path) as f:
    test_json = json.loads(f.read())

    with pytest.raises(ValidationError):
      validate(instance=test_json, schema=schema)
