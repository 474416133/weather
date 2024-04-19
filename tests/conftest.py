#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> conftest
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 21:43
@Desc   ：
"""
import pytest
from app.common.http_client import APIClient


@pytest.fixture()
def client_conf():
    return {
        'host': 'http://v1.yiketianqi.com',
        'app_id': '47187436',
        'app_secret': 'Z3Y5WqcJ4',
        'version': 'v63'
    }


@pytest.fixture()
def client(client_conf):
    with APIClient(**client_conf) as client:
        yield client

