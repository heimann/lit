from setuptools import setup

setup(
    name='lit',
    version='0.1',
    py_modules='lit',
    install_requires=[
        'Click',
        'phue',
    ],
    entry_points='''
        [console_scripts]
        lit=lit:main
    ''',
)
