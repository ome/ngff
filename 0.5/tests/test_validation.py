import json
import glob
import os

from dataclasses import dataclass
from typing import List

import pytest

from jsonschema import RefResolver, Draft202012Validator as Validator
from jsonschema.exceptions import ValidationError

schema_store = {}
for schema_filename in glob.glob("schemas/*"):
    with open(schema_filename) as f:
        schema = json.load(f)
        schema_store[schema["$id"]] = schema

GENERIC_SCHEMA = schema_store[
    "https://ngff.openmicroscopy.org/0.5/schemas/ome_zarr.schema"
]

print(schema_store)


@dataclass
class Suite:
    schema: dict
    data: dict
    valid: bool = True

    def validate(self, validator) -> None:
        if not self.valid:
            with pytest.raises(ValidationError):
                validator.validate(self.data)
        else:
            validator.validate(self.data)

    def maybe_validate(self, validator) -> None:
        if self.valid:
            validator.validate(self.data)


def pytest_generate_tests(metafunc):
    """
    Generates tests for the examples/ as well as tests/ subdirectories.

    Examples:
        These tests evaluate all of the files under the examples/ directory
        using the configuration in the provided config file in order detect
        what should be run. It is assumed that all files are valid and complete
        so that they can be wholly included into the specification. The
        .config.json file in each directory defines which schema will be used.

    Validation:
        These test consumes https://github.com/json-schema-org/JSON-Schema-Test-Suite#structure-of-a-test
        styled JSON tests. Metadata in each test defines which schema is used
        and whether or not the block is considered valid.
    """
    if "suite" in metafunc.fixturenames:
        suites: List[Schema] = []
        ids: List[str] = []
        schema_store = {}
        for filename in glob.glob("schemas/*.schema"):
            with open(filename) as o:
                schema = json.load(o)
            schema_store[schema["$id"]] = schema

        # Validation
        for filename in glob.glob("tests/*.json"):
            with open(filename) as o:
                suite = json.load(o)
            schema = suite["schema"]
            with open(schema["id"]) as f:
                schema = json.load(f)
            for test in suite["tests"]:
                ids.append("validate_" + str(test["formerly"]).split("/")[-1][0:-5])
                suites.append(Suite(schema, test["data"], test["valid"]))

        # Examples
        for config_filename in glob.glob("examples/*/.config.json"):
            with open(config_filename) as o:
                data = json.load(o)
            schema = data["schema"]
            with open(schema) as f:
                schema = json.load(f)
            example_folder = os.path.dirname(config_filename)
            for filename in glob.glob(f"{example_folder}/*.json"):
                with open(filename) as f:
                    # Strip comments
                    data = "".join(
                        line for line in f if not line.lstrip().startswith("//")
                    )
                    data = json.loads(data)
                    data = data["attributes"]  # Only validate the attributes object
                ids.append("example_" + str(filename).split("/")[-1][0:-5])
                suites.append(Suite(schema, data, True))  # Assume true

        metafunc.parametrize("suite", suites, ids=ids, indirect=True)


@pytest.fixture
def suite(request):
    return request.param


def test_run(suite):
    resolver = RefResolver.from_schema(suite.schema, store=schema_store)
    validator = Validator(suite.schema, resolver=resolver)
    suite.validate(validator)


def test_generic_run(suite):
    resolver = RefResolver.from_schema(GENERIC_SCHEMA, store=schema_store)
    validator = Validator(GENERIC_SCHEMA, resolver=resolver)
    suite.maybe_validate(validator)


def test_example_configs():
    """
    Test that all example folders have a config file
    """
    missing = []
    for subdir in os.walk("examples"):
        has_examples = glob.glob(f"{subdir[0]}/*.json")
        has_config = glob.glob(f"{subdir[0]}/.config.json")
        if has_examples and not has_config:
            missing.append(subdir[0])
    if missing:
        raise Exception(f"Directories missing configs: {missing}")
