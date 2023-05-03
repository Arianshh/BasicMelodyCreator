from setuptools import setup, find_packages

setup(
    name='basic_melody_generator',
    version='0.1',
    description='Generate Melodies Using X, Y coordinates',
    author='Arian Shariat',
    author_email='arian.shariat@gmain.com',
    packages=find_packages(),
    install_requires=[
        'pygame',
        'numpy',
    ]
)
