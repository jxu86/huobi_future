#!/usr/bin/env python3
# from setuptools import setup

# setup(
#     name="huobi-future-client",
#     version="0.1",
#     packages=['huobi', 'huobi.impl', 'huobi.impl.utils', 'huobi.exception', 'huobi.model'],
#     install_requires=['requests', 'apscheduler', 'websocket', 'websocket-client', 'urllib3']
# )

from setuptools import find_packages, setup

setup(
    name='huobi_future',
    description='huobi future sdk',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    test_suite="tests",
    zip_safe=False)
