from distutils.core import setup

setup(
    name='ddg',
    version='0.1.0',
    author='justinls',
    author_email='heartlessjunkie@gmail.com',
    packages=['ddg.duckduckgo'],
    url='http://pypi.python.org/pypi/ddg/',
    license='LICENSE.txt',
    description='www.duckduckgo.com zero click api for your shell',
    long_description=open('README.txt').read(),
    install_requires=[
        "Python >= 2.7.3",
    ],
)