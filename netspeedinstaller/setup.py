from setuptools import setup, find_packages

setup(
    name='netspeedinstaller',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'netspeedinstaller=netspeedinstaller.cli:main',
        ],
    },
    description='A command-line tool to download and install applications from the internet for fun!',
    author='Sojoyork/amricanboi/RussianDude',
    author_email='aimaankhankvs@gmail.com',
    url='https://github.com/yourusername/netspeedinstaller',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
