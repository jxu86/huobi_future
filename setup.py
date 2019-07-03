#!/usr/bin/env python3
from setuptools import setup

setup(
    name="huobi-future-client",
    version="0.1",
    packages=['huobi', 'huobi.impl', 'huobi.impl.utils', 'huobi.exception', 'huobi.model'],
    install_requires=['requests', 'apscheduler', 'websocket', 'websocket-client', 'urllib3']
)

