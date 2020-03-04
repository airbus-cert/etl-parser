#!/usr/bin/env python3

from setuptools import setup

setup(
    name="etl-parser",
    version="1.0.0",
    description="Event Trace Log file parser in pure Python",
    long_description="""`etl-parser` is a pure python 3 parser library for `ETL` Windows log files. `ETL` is the default format for [ETW](https://docs.microsoft.com/en-us/windows/win32/etw/event-tracing-portal).
But It's also the default format for the Kernel logger.

`etl-parser` has no system dependencies, and will work well on both Windows and Linux.

Since this format is not documented, we merged information from the blog of [Geoff Chappel](https://www.geoffchappell.com/) and reverse engineering activities conducted by Airbus CERT team.

What is `ETL` and why is it a pain to work with? Consider `ETL` as a container, like `AVI` is for video files. Reading `ETL` is similarly frustrating as reading an `AVI` file without the right codec.

`etl-parser` tries to solve this problem by including parsers for the following well known log formats:
* ETW manifest base provider
* TraceLogging
* MOF for kernel log
    """,
    author="Airbus CERT",
    author_email="cert@airbus.com",
    python_requires=">=3.6",
    packages=[
        "etl",
        "etl.parsers",
        "etl.parsers.etw",
        "etl.parsers.kernel"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
        "Intended Audience :: Information Technology"
    ],
    scripts=[
        "bin/etl2pcap",
        "bin/etl2xml"
    ],
    install_requires=[
        'construct'
    ]
)