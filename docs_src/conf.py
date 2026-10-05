# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PsychoPy Example Plugin'
copyright = '2024, Open Science Tools Ltd.'
author = 'Open Science Tools Ltd.'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# BF: Mock gltools so the docs build does not segfault:
#
# As observed with PsychoPy 2026.2, pyglet 1.5.27 and Sphinx 8.1 (Python 3.10):
# Building the docs crashes (segfault during `sphinx-build docs_src docs -b dirhtml`).
#
# The likely cause: Sphinx imports psychopy.visual to document the plugin,
# which imports psychopy.tools.gltools, which queries OpenGL at import time.
# When Sphinx is loaded, pyglet skips creating its hidden window (the "shadow window"),
# so no OpenGL context exists and the query crashes.
# Mocking that module avoids the query, so psychopy.visual can still be imported and thus documented.
#
# This is a temporary workaround. It should be removed once psychopy.tools.gltools
# no longer queries OpenGL at import time (which triggers this crash).

import sys
from unittest import mock

sys.modules['psychopy.tools.gltools'] = mock.MagicMock()


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'psychopy'
