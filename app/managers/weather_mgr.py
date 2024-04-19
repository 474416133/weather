#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> weather
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 23:04
@Desc   ：
"""
import logging
from app import settings
from app.common.http_client import APIClient
from app.errors_predefined import ERROR
from app.models.weather import create_weather_from_tq


logger = logging.getLogger('web')
api_client = APIClient(host=settings.TQ_HOST,
                       app_id = settings.TQ_APP_ID,
                       app_secret = settings.TQ_APP_SECRET)


def get_city_weather(city=None):
    """
    根据city查询
    :param city:
    :return:
    """
    params = {}
    if city:
        params['city'] = city

    ret =  api_client.get('/api', params=params)
    if 'errcode' in ret:
        logger.error('天气api调用失败, 返回错误码: {}, 错误信息:{}'.format(ret.get('errcode'),
                                                                      ret.get('errmsg')))
        raise ERROR.TA_API_INVOKE_ERROR('天气api调用失败')
    return create_weather_from_tq(**ret)