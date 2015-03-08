# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="eavatar.channel",
    version="0.1.0",
    description="EAvatar Channel - The channel service",
    # package_dir={'': ''},
    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    zip_safe=False,

    author="Sam Kuo",
    author_email="sam@eavatar.com",
    url="http://www.eavatar.com",

    entry_points={
        'console_scripts': [
            'ava-channel = server:main',
        ],
    },
)