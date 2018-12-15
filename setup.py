from setuptools import setup

setup(
    name='stsv',
    version='0.5',
    description='Pack for easy picture selection',
    license='MIT',
    url='www.github.com/mikegpl',
    author='Michał Grabowski',
    author_email='mkg.grabowski@gmail.com',
    packages=['stsv'],
    install_requires=['numpy', 'argparse', 'opencv-python'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'stsv = stsv.main:run'
        ]
    }
)
