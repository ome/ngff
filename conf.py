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

extensions = [
    "myst_parser",
    "sphinx_reredirects",
    "sphinx_design",
    "sphinxcontrib.bibtex",
]
bibtex_bibfiles = ["references.bib"]
source_suffix = [".rst", ".md"]
myst_heading_anchors = 5
myst_enable_extensions = ["deflist", "strikethrough", "colon_fence"]

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
    "about/index": "../index.html",
    "0.1/": "../specifications/0.1/index.html",
    "0.2/": "../specifications/0.2/index.html",
    "0.3/": "../specifications/0.3/index.html",
    "0.4/": "../specifications/0.4/index.html",
    "0.5/": "../specifications/0.5/index.html",
    "latest/index": "../specifications/0.5/index.html",
    "latest/": "../specifications/0.5/index.html",
    "dev/index": "../specifications/dev/index.html",
    "dev/": "../specifications/dev/index.html",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "header_links_before_dropdown": 6,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/ome/ngff",
            "icon": "fab fa-github",
            "type": "fontawesome",
        },
    ],
    "use_download_button": True,
}

html_favicon = "images/favicon-16x16.png"

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


def build_served_html(clean_up=True):
    import glob
    import subprocess
    import sys
    import os
    import shutil
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    
    # Create .htaccess to serve schemas inline (not download)
    os.makedirs("_html_extra", exist_ok=True)

    # Fetch GitHub tags and download schemas
    result = subprocess.check_output([
        "git", "ls-remote", "--tags", "https://github.com/ome/ngff-spec"
    ], text=True, timeout=10)
    tags = [
        line.split()[1].replace("refs/tags/", "").rstrip("^{}")
        for line in result.strip().split("\n") if line
        ]

    # Clone repo once, checkout each tag (faster than per-tag tarball download)
    repo_path = "_temp_ngff_spec"
    if not os.path.exists(repo_path):
        subprocess.check_call(["git", "clone", "https://github.com/ome/ngff-spec", repo_path])
    
    for tag in sorted(set(tags)):
        schema_dir = f"_html_extra/{tag}/schemas"
        os.makedirs(schema_dir, exist_ok=True)
        try:
            subprocess.check_call(["git", "-C", repo_path, "checkout", tag], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            src_schemas = glob.glob(os.path.join(repo_path, "**", "*.schema"), recursive=True)

            if len(src_schemas) == 0:
                print(f"⚠️  No schemas found for {tag}")
                continue

            for schema_file in src_schemas:
                dest_file = os.path.join(schema_dir, os.path.basename(schema_file))
                shutil.copy2(schema_file, dest_file)
                shutil.copy2(schema_file, dest_file + '.json')  # dual format
            print(f"✅ Checked out schemas for {tag}")
        except Exception as e:
            print(f"⚠️  Could not checkout {tag}: {e}")
    if clean_up:
        shutil.rmtree(repo_path, ignore_errors=True)

    # Build specifications from local submodules
    displayed_spec_versions = [
        d
        for d in os.listdir("specifications")
        if os.path.isdir(os.path.join("specifications", d))
    ]

    for version in displayed_spec_versions:

        # find 'pre_build.py' in 'specifications' subdirectories
        script = glob.glob(f"specifications/{version}/**/pre_build.py", recursive=True)[
            0
        ]

        # Inject shared OME boilerplate next to index.bs so the legacy Bikeshed
        # build renders OME branding instead of falling back to the W3C default.
        # Kept here in the superproject so we never have to edit, commit, and
        # bump every ngff-spec version submodule (the includes were lost exactly
        # that way during the ngff -> ngff-spec migration).
        spec_dir = os.path.dirname(script)
        for inc in ("header.include", "copyright.include"):
            src = os.path.join("boilerplate", inc)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(spec_dir, inc))
                print(f"✅ Injected {inc} for version {version}")
            else:
                print(
                    f"⚠️  Missing boilerplate/{inc}; {version} will use Bikeshed defaults"
                )

        subprocess.check_call([sys.executable, script])
        print("✅ Built rendered examples/schemas for version", version)

        # copy schemas to _html_extra for served html
        schema_files = glob.glob(f"specifications/{version}/**/*.schema", recursive=True)
        for schema_file in schema_files:
            dest_dir = os.path.join("_html_extra", version, "schemas")
            os.makedirs(dest_dir, exist_ok=True)
            dest_file = os.path.join(dest_dir, os.path.basename(schema_file))
            shutil.copy2(schema_file, dest_file)
            shutil.copy2(schema_file, dest_file + '.json')  # dual format (json + schema)

        # build jupyter-book docs in specification submodules
        myst_file = glob.glob(f"specifications/{version}/**/myst.yml", recursive=True)[
            0
        ]
        bikeshed_output = f"specifications/{version}/index.html"

        # copy built html files to _html_extra
        try:
            if os.path.exists(bikeshed_output):
                shutil.copy2(bikeshed_output, f"_html_extra/{version}/index.html")
                print(f"✅ Found legacy bikeshed, serving as extra html for {version}")
        except Exception as e:
            print(f"⚠️  Could not copy served html for version {version}: {e}")


build_served_html()
