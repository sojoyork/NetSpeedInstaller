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
    description='A command-line tool to download and install applications from the internet.',
    author='Your Name',
    author_email='Sojoyork/amricanboi/RussianDude',
    url='https://github.com/sojoyork/NetSpeedInstaller',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
