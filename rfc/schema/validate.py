#!/usr/bin/env python3
"""Check the YAML front matter of the RFC documents against front_matter.yaml.

Run it over everything, or over the files you are working on:

    python rfc/schema/validate.py
    python rfc/schema/validate.py rfc/9/index.md

Needs `pip install linkml`. Exits non-zero and lists every problem it found.
"""

import datetime
import sys
from pathlib import Path

import yaml
from linkml.validator import validate

SCHEMA = Path(__file__).with_name("front_matter.yaml")
RFC_DIR = SCHEMA.parent.parent
SECTIONS = ("reviews", "comments", "responses")


def documents():
    """Every RFC document that must carry front matter, as (path, class) pairs.

    Skipped on purpose: `versions/` (archived copies of earlier drafts, which keep
    no front matter of their own), `templates/` (placeholders such as YYYY-MM-DD),
    and the `index.md` of each section, which is only a toctree.
    """
    for rfc in sorted(RFC_DIR.glob("*/index.md")):
        if rfc.parent.name.isdigit():
            yield rfc, "RFCFrontMatter"
            for section in SECTIONS:
                for path in sorted(rfc.parent.glob(f"{section}/*/index.md")):
                    yield path, "ReviewFrontMatter"


def front_matter(path):
    """The parsed front matter, or a string explaining why it could not be read."""
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        return "no YAML front matter (the file must open with a `---` block)"
    try:
        return _as_strings(yaml.safe_load(parts[1]) or {})
    except yaml.YAMLError as error:
        return f"front matter is not valid YAML: {error}"


def _as_strings(value):
    """Turn the dates PyYAML parses back into ISO strings.

    An unquoted `date: 2025-07-02` becomes a datetime.date, while a quoted one
    stays text; the pages treat both the same, so validation should too.
    """
    if isinstance(value, dict):
        # A key written with nothing after it (`recommendation:`, which the review
        # template allows) means "not provided", so drop it rather than validate None.
        return {k: _as_strings(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [_as_strings(v) for v in value]
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    return value


def check(path, target_class):
    """Problems found in one document, as a list of strings."""
    meta = front_matter(path)
    if isinstance(meta, str):
        return [meta]
    report = validate(meta, str(SCHEMA), target_class, strict=False)
    return [result.message for result in report.results]


def main(argv):
    wanted = {Path(a).resolve() for a in argv}
    checked = failed = 0
    for path, target_class in documents():
        if wanted and path.resolve() not in wanted:
            continue
        checked += 1
        problems = check(path, target_class)
        failed += bool(problems)
        for problem in problems:
            print(f"{path}: {problem}")

    missed = wanted - {p.resolve() for p, _ in documents()}
    for path in sorted(missed):
        print(f"{path}: not an RFC document this script validates")

    print(f"\n{checked} document(s) checked, {failed} with problems")
    return 1 if failed or missed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
