import json
from pprint import pprint
from pyld import jsonld


with open("schemas/jsonld/frame.json") as o:
    frame = json.load(o)


with open("examples/image/valid/image_metadata.json") as o:
    data = json.load(o)


def frame_with_options(data, frame, options=None):
    if options is None:
        options = dict()
    return jsonld.frame(
        data,
        frame,
        options)

def test_insertion():
    pprint(data)
    data["@context"] = frame["@context"]
    r = frame_with_options(data, frame)
    pprint(r)
    assert "@type" in r["ngff:multiscales"][0], r
    assert "@type" in r["ngff:multiscales"][0]["ngff:datasets"][0], r

def test_pass_context():
    pprint(data)
    with open("schemas/jsonld/context.json") as o:
        context = json.load(o)
    r = frame_with_options(data, frame, options={
            "context": context,
        })
    pprint(r)
    assert "@type" in r["ngff:multiscales"][0], r
    assert "@type" in r["ngff:multiscales"][0]["ngff:datasets"][0], r
