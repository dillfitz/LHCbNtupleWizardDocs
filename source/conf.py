import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from sphinx_config import *

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Ntuple Wizard Documentation"
copyright = "2023, LHCb"
author = "LHCb"
#release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "README"
source_suffix = [".md"]
exclude_patterns += ['README']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = "furo"
html_static_path = ["_static"]
html_css_files = [ 'wizard.css', ]
