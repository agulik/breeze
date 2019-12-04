from setuptools import setup

setup(
    name='breeze',
    version='0.1',
    author='Andrew Gulik',
    author_email='andrewgulik@gmail.com',
    description='Breeze is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    url='https://github.com/agulik/breeze',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        breeze=breeze:cli
    '''
)
