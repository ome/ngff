# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NGFF'
copyright = '2023, NGFF Community'
author = 'NGFF Community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
source_suffix = [".rst", ".md"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git', '.pytest_cache', '**/.pytest_cache', '**/.tox', 'README.md', 'LICENSE.md', 'CONTRIBUTING.md']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']


# Run bikeshed build
import glob
import os
import subprocess
import shutil


for index_file in ["latest/index.bs"] + glob.glob("[0-9]*/index.bs"):

    output_file = index_file.replace("bs", "html")

    src_time = os.path.getmtime(index_file)
    if os.path.exists(output_file):
        out_time = os.path.getmtime(output_file)
        if src_time < out_time:
            print(f"Skipping unchanged {index_file}")
            continue

    subprocess.check_call(f"bikeshed  spec {index_file} {output_file}", shell=True)

    dir_name = index_file.split("/")[0]
    os.makedirs(f"_build/{dir_name}", exist_ok=True)
    shutil.copyfile(output_file, f"_build/{output_file}")
