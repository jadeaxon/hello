try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jeff Anderson',
    'url': 'project URL',
    'download_url': 'download URL',
    'author_email': 'jadeaxon@hotmail.com',
    'version': '0.1'
    'install_requires': ['nose'],
    'scripts': [],
    'packages': ['NAME'],
    'name': 'project name'
}

setup(**config)


