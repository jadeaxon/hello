try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An exercise from the book.',
    'author': 'Jeff Anderson',
    'url': 'project URL',
    'download_url': 'download URL',
    'author_email': 'jadeaxon@hotmail.com',
    'version': '0.1'
    'install_requires': ['pytest'],
    'scripts': [],
    'packages': ['ex47'],
    'name': 'LP3THW Exercise 47'
}

setup(**config)


