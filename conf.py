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
    "sphinxcontrib.bibtex"]
bibtex_bibfiles = ["references.bib"]
source_suffix = [".rst", ".md"]
myst_heading_anchors = 5
myst_enable_extensions = [
    "deflist",
    "strikethrough",
    "colon_fence"
    ]

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
    versions = [d for d in os.listdir("specifications") if os.path.isdir(os.path.join("specifications", d))]

    for version in versions:

        # copy schemas to _html_extra
        os.makedirs(f'_html_extra/{version}/schemas', exist_ok=True)
        schemas = glob.glob(f'specifications/{version}/**/*.schema', recursive=True)
        for schema in schemas:
            shutil.copy2(schema, f'_html_extra/{version}/schemas/')
        print(f'✅ Copied schemas for version {version}')
    
        # find 'pre_build.py' in 'specifications' subdirectories
        script = glob.glob(f'specifications/{version}/**/pre_build.py', recursive=True)[0]

        subprocess.check_call([sys.executable, script])
        print('✅ Built rendered examples/schemas for version', version)

        # build jupyter-book docs in specification submodules
        myst_file = glob.glob(f'specifications/{version}/**/myst.yml', recursive=True)[0]
        if os.path.exists(myst_file):
            cdir = os.getcwd()
            try:
                os.chdir(os.path.dirname(myst_file))
                subprocess.check_call(['jupyter-book', 'build', '--ci', '--html'])
            finally:
                os.chdir(cdir)
        print('✅ Built jupyter-book documentation for version', version)


        # copy built html files to _html_extra
        bikeshed_output = f'specifications/{version}/index.html'
        try:
            if os.path.exists(bikeshed_output):
                shutil.copy2(bikeshed_output, f'_html_extra/{version}/index.html')
                print(f'✅ Found legacy bikeshed, serving as extra html for {version}')
            else:
                build_dir = glob.glob(f'specifications/{version}/**/_build/html', recursive=True)[0]
                shutil.copytree(build_dir, f'_html_extra/{version}', dirs_exist_ok=True)
                print(f'✅ Copying jupyter-book documentation as extra html for {version}')
        except Exception as e:
            print(f'⚠️  Could not copy served html for version {version}: {e}')

build_served_html()
    