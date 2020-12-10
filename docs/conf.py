# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.append('../')
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../sospcat'))


# -- Project information -----------------------------------------------------

project = 'SoSpaCATpy'
copyright = '2020, Jonas I. Liechti'
author = 'Jonas I. Liechti'

# ############################################################################
# ############################################################################
# The full version, including alpha/beta/rc tags


def get_version_and_cmdclass(package_path):
    """Load version.py module without importing the whole package.

    Template code from miniver
    """
    import os
    from importlib.util import module_from_spec, spec_from_file_location

    spec = spec_from_file_location(
            "version", os.path.join(package_path, "_version.py")
        )
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__  # , module.cmdclass


# major/minor
_release = get_version_and_cmdclass('../sospcat')
print(_release)
release = _release.split('+')[0]
version = '.'.join(release.split('.')[:2])
# ############################################################################
# ############################################################################

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'm2r2'
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# ############################################################################
# ############################################################################
source_suffix = ['.rst', '.md']
master_doc = 'index'
todo_include_todos = True
# ############################################################################
# ############################################################################

# ############################################################################
# ############################################################################
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# ############################################################################
# ############################################################################


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# ############################################################################
# ############################################################################
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
        'numpy': ('http://docs.scipy.org/doc/numpy/', None),
        'matplotlib': ('http://matplotlib.org', None),
        'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
        'sklearn': (
            'http://scikit-learn.org/stable',
            (None, './_intersphinx/sklearn-objects.inv')
        )
        }
# ############################################################################
# ############################################################################

# ############################################################################
# ############################################################################
# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False
# ############################################################################
# ############################################################################
# Use both docstring of class and docstring of __init__ methods
autoclass_content = 'both'
