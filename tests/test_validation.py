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


class LDErr(Exception):
    pass


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 8000)


def test_json(method, testfile, httpserver):

    for uri, filename in (
        ("/context.json", "schemas/jsonld/context.json"),
        ("/image.schema", "schemas/image.schema"),
    ):
        with open(filename) as o:
            httpserver.expect_request(uri).respond_with_data(o.read())

    if "invalid" in testfile:
        with pytest.raises((JSErr, LDErr, SaladErr)):
            method(testfile)
            if "invalid_axes_order" in testfile:
                pytest.skip("not supported")

    else:
        method(testfile)


def files():
    return list(glob.glob(f"examples/*/valid/*.json")) + \
        list(glob.glob(f"examples/*/invalid/*.json"))

def ids():
    return [str(x).split("/")[-1][0:-5] for x in files()]


@pytest.fixture(params=files(), ids=ids())
def testfile(request):
    return request.param


@pytest.fixture(params=("jsonschema", "jsonld"))
def method(request):

    if request.param == "jsonschema":

        def json_schema(path):
            print("json_schema", path)
            schemaName = None
            for name in ['image', 'plate', 'well']:
                if name in path:
                    schemaName = name
            if schemaName is None:
                raise Exception("No schema found")
            with open(f'schemas/{schemaName}.schema') as f:
                schema = json.loads(f.read())

            with open(path) as f:
                test_json = json.loads(f.read())
            return js_valid(instance=test_json, schema=schema)

        return json_schema

    elif request.param == "salad":
        document_loader, avsc_names, schema_metadata, metaschema_loader = \
            load_schema('salad_schema/image.yml')

        def salad(path):
            load_and_validate(document_loader, avsc_names, path, strict=True)

        return salad

    else:
        with open('schemas/jsonld/shacl.ttl') as f:
            shacl = f.read()

        def jsonld(path):

            with open(path) as f:
                graph = f.read()

            graph = modify(graph)
            s = Graph().parse(data=shacl, format="turtle")
            d = Graph().parse(data=graph, format="json-ld")

            if False:
                print("=" * 100)
                for stmt in s:
                    import pprint
                    pprint.pprint(stmt)
                print("=" * 100)
                for stmt in d:
                    import pprint
                    pprint.pprint(stmt)
                print("=" * 100)

            conforms, report, message = ld_valid(
                data_graph=d,
                shacl_graph=s,
                advanced=True,
                debug=False,
                allow_warnings=True,
            )

            if not conforms:
                raise LDErr(message)

        return jsonld


def modify(data):
    print("BEFORE", data)
    data = json.loads(data)

    # Can be used to wrap collections
    # DISABLED: data = walk(data)

    # Framing can be used to inject @type attributes
    with open("schemas/jsonld/frame.json") as o:
        frame = json.load(o)
    options = dict()
    data["@context"] = frame["@context"]
    data = jsonld.frame(
        data,
        frame,
        options)
    data= {"@context": "http://localhost:8000/context.json#", "@graph": data}
    data = json.dumps(data, indent=4)  ## TODO: Seems wasteful
    print("AFTER", data)
    return data


def walk(data, path=None):

    if path is None:
        path = []

    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = walk(v, path + [k])

    elif isinstance(data, list):
        replacement = list()
        for idx, item in enumerate(data):
            if path[-1] == "@graph":
                replacement.append(walk(item, path))
            else:
                wrapper = {
                    "@type": "ngff:ListItem",
                    "ngff:position": idx
                }
                wrapper["ngff:item"] = walk(item, path + [idx])
                replacement.append(wrapper)
        data = replacement

    return data
