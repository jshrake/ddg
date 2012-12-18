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

setup(
    name='ddg',
    version='0.2.0',
    author='justinls',
    author_email='heartlessjunkie@gmail.com',
    packages=['duckduckgo'],
    scripts=['ddg.py'],
    url='https://github.com/justinls/ddg',
    license=open('LICENSE').read(),
    description='www.duckduckgo.com zero-click api for your command-line',
    long_description=open('README.rst').read(),
    install_requires=requires,
    entry_points=entry_points,
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
