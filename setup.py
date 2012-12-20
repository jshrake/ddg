from setuptools import setup

requires = []

try:
    import argparse
except ImportError:
    requires.append('argparse')

entry_points = {
    'console_scripts': [
        'ddg = ddg:main',
    ]
}

README = open('README.rst').read()
CHANGES = open('CHANGES.rst').read()

setup(
    # General Information
    name='ddg',
    version='0.2.2',
    author='Justin Shrake',
    author_email='justinshrake@gmail.com',
    description='DuckDuckGo zero-click api for your command-line',
    long_description=README + '\n' + CHANGES,
    url='https://github.com/justinls/ddg',
    license='MIT',

    # Add packages, scripts, and other data
    packages=['duckduckgo'],
    scripts=['ddg.py'],

    #define requirements and entry points
    install_requires=requires,
    entry_points=entry_points,

    #pypi classifiers
    classifiers=[
         'Development Status :: 4 - Beta',
         'Environment :: Console',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2.6',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
