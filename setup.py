# -*- coding: utf-8 -*-
import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires=[
    "TurboGears2 >= 2.1.4",
    "tgext.pluggable",
    "lxml",
    "webhelpers",
    "py3o.template",
    "pyjon.utils"
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='tgext.odt',
    version='0.3',
    description='tgext.odt is a Pluggable application for TurboGears2 that allows the rendering of .odt (openoffice/libreoffice) documents as an output templates.',
    long_description=README,
    author='Puria Nafisi Azizi',
    author_email='puria.nafisi@axant.it',
    url='https://github.com/puria/tgext.odt',
    keywords='turbogears2.extension',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'tgapp.tgextodt': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    """,
    zip_safe=False
)
