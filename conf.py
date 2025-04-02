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

extensions = ["myst_parser"]
source_suffix = [".rst", ".md"]
myst_heading_anchors = 5
myst_enable_extensions = ["deflist"]

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
]


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
    "_bikeshed",
]

# ####################################
# Run bikeshed build
# ####################################


def bikeshed():
    import glob
    import os
    import shutil
    import subprocess

    for index_file in ["latest/index.bs"] + glob.glob("[0-9]*/index.bs"):
        output_file = index_file.replace("bs", "html")
        output_dir = os.path.dirname(output_file)
        target_dir = os.path.join("_bikeshed", output_dir)

        run_bikeshed = True

        # Give the loop a chance to skip files if no build is needed/requested
        if "BIKESHED" not in os.environ and os.path.exists(output_file):
            src_time = os.path.getmtime(index_file)
            out_time = os.path.getmtime(output_file)
            if src_time < out_time:
                print(f"{index_file} unchanged")
                run_bikeshed = False

        if run_bikeshed:
            subprocess.check_call(
                f"bikeshed spec {index_file} {output_file}", shell=True
            )

        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree(output_dir, target_dir)


bikeshed()
del bikeshed
