#!/usr/bin/env python
import codecs
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


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
    return module.__version__, module.cmdclass


def find_packages():
    """adapted from IPython's setupbase.find_packages()"""
    packages = []
    for dir, subdirs, files in os.walk('sospcat'):
        package = dir.replace(os.path.sep, '.')
        if '__init__.py' not in files:
            # not a package
            continue
        # if sys.version_info < (3, 4)\
        #        and 'asyncio' in package and 'sdist' not in sys.argv:
        #     # Don't install asyncio packages on old Python
        #     # avoids issues with tools like compileall, pytest, etc.
        #     # that get confused by presence of Python 3-only sources,
        #     # even when they are never imported.
        #     continue
        packages.append(package)
    return packages


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def install_requires(req_file='requirements.txt'):
    with open(req_file, 'r') as fobj:
        requires = fobj.read().splitlines()
    # if sys.version_info > (3, 4):
    #     requires.extend(['websockets'])
    return requires


def get_readme(name='README.md'):
    r"""Return the content of the README file.

    By default it is assumed that the README file is in the same directory as
    setup.py.
    The README format is determined via the file extension and should be either
    `.md` or `.rst`. Any other format will lead to the content being processed
    as plain text.
    """
    with open(os.path.join(here, name), 'r') as fobj:
        readme_content = fobj.read()
    if name.endswith('.md'):
        long_description_content_type = 'text/markdown'
    elif name.endswith('.rst'):
        long_description_content_type = 'text/x-rst'
    else:
        long_description_content_type = 'text/plain'

    return readme_content, long_description_content_type


version, cmdclass = get_version_and_cmdclass("sospcat")
long_description, long_description_content_type = get_readme()


setup(
    name='SoSpCAT',
    version=version,
    cmdclass=cmdclass,
    packages=find_packages(),
    description='Social-Spatial Community Assignment Test',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url='https://SoSpcATPy.readthedocs.io',
    project_urls={
            "Bug Tracker": "https://github.com/j-i-l/SoSpCATpy/issues",
            "Documentation": 'https://sospcatpy.readthedocs.io',
            "Source Code": "https://github.com/j-i-l/SoSpCATpy",
        },
    author='Jonas I. Liechti [aut, cre]',
    author_email='jonas.i.liechti@gmail.com',
    license='BSD',
    install_requires=install_requires(),
    keywords='social spatial group cluster groupstructure',
    classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    # include_package_data=True,  # includes whatever is in MANIFEST.in
    # test_suite='tests',
)
