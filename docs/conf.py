import os
import sys

# Minimal required Sphinx settings
project = 'Static Site'
copyright = '2025, Your Name'
author = 'Your Name'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme is not important as its output will be overwritten
html_theme = 'alabaster'