from setuptools import setup, find_packages

setup(
    name='playText-cli',
    version='0.1',
    py_modules=['client'],
    install_requires=[
        'Click',
        'grpcio',
    ],
    entry_points='''
        [console_scripts]
        playText=client:playText
    ''',
)