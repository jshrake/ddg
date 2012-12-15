from distutils.core import setup

setup(
    name='ddg',
    version='0.1.0',
    author='justinls',
    author_email='heartlessjunkie@gmail.com',
    packages=['ddg, ddg.duckduckgo'],
    url='https://github.com/justinls/ddg',
    license='LICENSE.txt',
    description='www.duckduckgo.com zero click api for your shell',
    long_description=open('README.rst').read(),
    install_requires=[
        "Python >= 2.7.3",
    ],
)
