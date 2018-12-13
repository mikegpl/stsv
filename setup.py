from setuptools import setup

setup(
    name='stsv',
    version='0.1',
    description='Module for measuring time complexity of functions',
    license='MIT',
    url='www.github.com/mikegpl',
    author='Michał Grabowski',
    author_email='mkg.grabowski@gmail.com',
    packages=['stsv'],
    install_requires=['numpy', 'argparse', 'opencv-python'],
    entry_points={
        'console_scripts': [
            'stsv = stsv.main:run'
        ]
    }

)