# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "NGFF"
copyright = "2020-2025, NGFF Community"
author = "NGFF Community"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_reredirects"]
source_suffix = [".rst", ".md"]
myst_heading_anchors = 5
myst_enable_extensions = ["deflist", "strikethrough"]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".git",
    ".pytest_cache",
    "**/.pytest_cache",
    "**/.tox",
    "README.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
    "**/README.md",
    "**/LICENSE.md",
    "**/CONTRIBUTING.md",
]

redirects = {
     "tools/index": "../resources/tools/index.html",
     "publications/index": "../resources/publications/index.html",
     "data/index": "../resources/data/index.html",
     "about/index": "../index.html"
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"

html_static_path = ["_static"]

html_css_files = [
    "https://cdn.datatables.net/v/dt/dt-1.11.5/datatables.min.css",
]

html_js_files = [
    "https://cdn.datatables.net/v/dt/dt-1.11.5/datatables.min.js",
    "main.js",
]

html_extra_path = [
    "_html_extra",
]

# ####################################
# Post-process all versions
# ####################################



from pathlib import Path

from json_schema_for_humans.generate import (
    generate_from_filename,
    GenerationConfiguration,
)


def get_version_index_html(*, version: str, schmea_fnames: list[Path]) -> str:
    schemas_list = "\n".join(
        [f"<li><a href={p.name}>{p.stem}</a> </li>" for p in schmea_fnames]
    )
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Overpass:300,400,600,800">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="schema_doc.css">
    <script src="https://use.fontawesome.com/facf9fa52c.js"></script>
    <script src="schema_doc.min.js"></script>
    <meta charset="utf-8"/>


    <title>OME-zarr version {version}</title>
</head>
<body onload="anchorOnLoad();" id="root">

    <div class="breadcrumbs"></div> <h1>Version {version}</h1><br/>
    <ul>
    {schemas_list}
    </ul>
</body>
</html>
"""


def get_index_html(*, versions: list[str]) -> str:
    versions_list = "\n".join(
        [f"<li><a href={v}/index.html>{v}</a> </li>" for v in versions]
    )
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Overpass:300,400,600,800">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="schema_doc.css">
    <script src="https://use.fontawesome.com/facf9fa52c.js"></script>
    <script src="schema_doc.min.js"></script>
    <meta charset="utf-8"/>


    <title>OME-zarr JSON schema specifications</title>
</head>
<body onload="anchorOnLoad();" id="root">

    <div class="breadcrumbs"></div> <h1>OME-zarr JSON schema specifications</h1><br/>
    <p> Nicely rendered JSON schemas generated directly from the <a href=https://ngff.openmicroscopy.org/specifications/index.html>OME-zarr specifications</a>.</p>
    <p> Generated using <a href=https://coveooss.github.io/json-schema-for-humans>json-schema-for-humans</a>.</p>
    <ul>
    {versions_list}
    </ul>
</body>
</html>
"""


def gen_version(version):
    version_path = Path(version)
    schema_path = version_path / "schemas"
    for schema_file in sorted(schema_path.glob("*.schema")):
        print(schema_file)
        generate_from_filename(
            schema_file,
            result_file_name=schema_path / schema_file.with_suffix(".html").name,
            config=GenerationConfiguration(template_name="js", with_footer=False),
        )

    schema_fnames = [
        p
        for p in sorted(schema_path.glob("*.html"))
        if p.name != "index.html"
    ]
    with open(schema_path / "index.html", "w") as f:
        f.write(
            get_version_index_html(version=version, schmea_fnames=schema_fnames)
        )


def post_process():
    import glob
    import os
    import shutil
    import subprocess
    import sys

    # build ngff-spec docs
    ngff_spec_versions = [
        {"submodule": "specifications/0.5", "target": "0.5"},
        {"submodule": "specifications/0.6.dev2", "target": "0.6.dev2"},
    ]

    serve_directory = "_html_extra"
    shutil.rmtree(serve_directory, ignore_errors=True)
    os.makedirs(serve_directory, exist_ok=True)

    for spec_version in ngff_spec_versions:
        submodule_dir = spec_version["submodule"]
        target_dir = spec_version["target"]

        if os.path.exists(submodule_dir):
            print(f"Building ngff-spec docs for version {target_dir}...")

            os.chdir(submodule_dir)

            # prebuild ngff-spec examples and schemas
            subprocess.check_call([sys.executable, "ngff_spec/pre_build.py"])
            os.chdir("ngff_spec")

            # Set BASE_URL from environment (for GitHub Pages) or fallback
            os.environ["§BASE_URL"] = f"/{target_dir}/"
            subprocess.check_call(["jupyter", "book", "build", "--ci", "--html"])
            os.chdir("../../..")

            # copy built ngff-spec to _html_extra for serving
            source = Path(submodule_dir) / "ngff_spec" / "_build" / "html"
            target = Path(serve_directory) / target_dir
            shutil.copytree(source, target)

            # copy examples and schemas to bikeshed output
            schema_files = glob.glob(os.path.join(
                submodule_dir, "ngff_spec/schemas", '*.schema'), recursive=True)
            target = Path(serve_directory) / target_dir / "schemas"
            os.makedirs(target, exist_ok=True)

            for schema_file in schema_files:
                shutil.copy2(schema_file, target)


post_process()
del post_process
