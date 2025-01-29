# conf.py for Jupyter Book

import os
import sys
import asyncio
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Fix Tornado AsyncIO issue on Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('.'))

# General project information
project = 'Tabelle Fallstudie 2'
author = 'Your Name'
release = '0.1'

# Extensions
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

# Source file parsing
source_suffix = ['.rst', '.md']
master_doc = 'index'

# HTML options
html_theme = 'alabaster'
