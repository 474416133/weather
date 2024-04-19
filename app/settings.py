#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> settings
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/16 16:46
@Desc   ：
"""
import  os

APP_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(APP_PATH)


LOG_OPTIONS = {
    'path': os.sep.join([PROJECT_PATH, 'logs'])
}


prod = os.getenv('ENV') or 'dev'

SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"\xb7Q\x9d\xa9*\xd0u\xb02\xddP\x84'\r\x96T\x8f\\\xfa\x1c\x02\x85P\x9f"
FLASK_ADMIN_SWATCH = 'cerulean'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
DATE_FORMAT = '%Y-%m-%d'


#
TQ_APP_ID = '47187436'
TQ_APP_SECRET = 'Z3Y5WqcJ'
TQ_HOST = 'http://v1.yiketianqi.com'

