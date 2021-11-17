
import os
import json

import pytest
from schema_salad.schema import load_schema, load_and_validate
from schema_salad.validate import validate
from schema_salad.exceptions import ValidationException

# NB: Need to have contents of /json_schema served at localhost:8000
# so that http://localhost:8000/omero.schema.json is valid

# cd json_schema
# python -m http.server

document_loader, avsc_names, schema_metadata, metaschema_loader = load_schema('salad_schema/image.yml')


# Test valid files
invalid_paths = [entry.path for entry in os.scandir("examples/valid")]
@pytest.mark.parametrize("path", invalid_paths)
def test_valid(path):
  load_and_validate(document_loader, avsc_names, path, strict=True)

# Test invalid files
invalid_paths = [entry.path for entry in os.scandir("examples/invalid")]
@pytest.mark.parametrize("path", invalid_paths)
def test_invalid(path):
  with pytest.raises(ValidationException):
    load_and_validate(document_loader, avsc_names, path, strict=True)
