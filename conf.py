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


def build_served_html():
    import glob
    import subprocess
    import sys
    import os
    import shutil
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    
    # Fetch GitHub tags and download schemas
    try:
        result = subprocess.check_output([
            "git", "ls-remote", "--tags", "https://github.com/ome/ngff-spec"
        ], text=True, timeout=10)
        tags = [line.split()[1].replace("refs/tags/", "").rstrip("^{}") for line in result.strip().split("\n") if line]
        for tag in sorted(set(tags)):
            schema_dir = f"_html_extra/{tag}/schemas"
            os.makedirs(schema_dir, exist_ok=True)
            # Download schemas from GitHub raw for this tag
            gh_url = f"https://github.com/ome/ngff-spec/archive/refs/tags/{tag}.tar.gz"
            try:
                import tempfile, tarfile
                with tempfile.NamedTemporaryFile(delete=False) as tmp:
                    subprocess.check_call(["curl", "-sL", gh_url, "-o", tmp.name])
                    with tarfile.open(tmp.name) as tar:
                        for member in tar.getmembers():
                            if "/schemas/" in member.name and member.name.endswith(".schema"):
                                # Extract just the filename, flatten into schema_dir
                                target = os.path.join(schema_dir, os.path.basename(member.name))
                                tar.extract(member, path=tempfile.gettempdir())
                                src = os.path.join(tempfile.gettempdir(), member.name)
                                shutil.copy2(src, target)
                    os.unlink(tmp.name)
                print(f"✅ Downloaded schemas for {tag}")
            except Exception as e:
                print(f"⚠️  Could not download schemas for {tag}: {e}")
    except Exception:
        pass
    
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
