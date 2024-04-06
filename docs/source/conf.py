# Configuration file for the Sphinx documentation builder.
# Exclude base script files (the theme uses its own)
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.script_files = []
# -- Project information

project = 'Пароль на Python'
copyright = '2024, JV&LN'
author = 'JV&LN'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_static_path = ['_static']

StandaloneHTMLBuilder.supported_image_types = [
'image/svg+xml',
'image/gif',
'image/png',
'image/jpeg']
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
