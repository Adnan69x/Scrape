from setuptools import setup, find_packages

setup(
    name='Scrape',
    version='1.0.0',
    description='Your Telegram bot description',
    long_description='Long description of your Telegram bot',
    author='Adnan',
    author_email='adnan@gmail.com',
    url='https://github.com/Adnan69x/Scrape',
    packages=find_packages(),
    install_requires=[
        'telethon',
        # Add any other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
