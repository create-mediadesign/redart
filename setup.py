from setuptools import setup
setup(
    name = 'redart',
    version = '0.1.0',
    packages = ['redart'],
    description = 'A Redmine Artifact manager',
    author = 'René Groß',
    author_email = 'rg@create.at',
    license = 'GNU GENERAL PUBLIC LICENSE v3',
    install_requires = [
      'click',
      'python-redmine'
    ],
    entry_points = {
        'console_scripts': [
            'redart = redart.__main__:cli'
        ]
    })