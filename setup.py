"""
setuptools module for project.
"""

import setuptools

setuptools.setup(
    name="fishnchips",
    version="0.1.0",
    url="https://github.com/caglartoklu/fishnchips",

    author="Caglar Toklu",
    author_email="caglartoklu@gmail.com",

    description="Fish n Chips",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
        'console_scripts': ['fishn=fishnchips.command_line:main'],
    },

    test_suite='nose.collector',
    tests_require=['nose'],

    include_package_data=True,
    zip_safe=False,
)
