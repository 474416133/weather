#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> test_http_client
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 21:40
@Desc   ：
"""
import json
import pytest


@pytest.mark.parametrize('city',
                         ['广州'])

def test_get_weather(client, city):
    resp_json = client.get('/api', params={'city': city})
    print(json.dumps(resp_json, indent=2, ensure_ascii=False))
    assert resp_json['city'] == city



if __name__ == '__main__':
    pytest.main(["-s", "test_get_weather.py::test_get_weather"])
