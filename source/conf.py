# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = 'imputegap'
copyright = '2025, Quentin Nater'
author = 'Quentin Nater'
html_title = 'A Hands-on Tutorial on Time Series Imputation with ImputeGAP'
html_short_title = "Tutorials"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    'sphinx_tabs.tabs'
]

autosummary_generate = True  # Automatically generate method summaries

html_static_path = ['_static']

html_logo = "_static/logo.png"

html_favicon = "https://www.naterscreations.com/imputegap/favicon.png"

html_css_files = ['custom.css']

html_title = "ImputeGAP Tutorials - KDD'25"


templates_path = ['_templates']
exclude_patterns = []


html_theme = "sphinx_material"


html_theme_options = {
    "nav_title": "ImputeGAP Tutorials - KDD'25",
    "color_primary": "blue-grey",
    "color_accent": "teal",
    "repo_url": "https://github.com/eXascaleInfolab/ImputeGAP/",
    "repo_name": "GitHub",
    "nav_links": [
        {"href": "schedule.html", "title": "Schedule"},
        {"href": "slides_codes.html", "title": "Slides & Code"},
        {"href": "presenters.html", "title": "Presenters"},
        {"href": "https://kdd2025.kdd.org/", "title": "KDD'25", "internal": False},
    ],

}

html_context = {
    "github_user": "eXascaleInfolab",
    "github_repo": "https://github.com/eXascaleInfolab/ImputeGAP",
    "display_github": True,
}

html_show_sourcelink = False


napoleon_google_docstring = True
napoleon_numpy_docstring = False


sys.path.insert(0, os.path.abspath('../../../'))  # Adjust path to the project root
