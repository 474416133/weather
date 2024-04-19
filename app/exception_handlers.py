#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> exception_handlers
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 18:21
@Desc   ：
"""
import logging
from flask import request
from werkzeug.exceptions import HTTPException
from app.common.response import FAIL
from app.common.errors import BizError


logger = logging.getLogger('error')

def handle_http_exception(e):
    logger.exception('httperror.')
    if 'api' in request.url:
        return FAIL(err_code=e.code, err_msg=e.description)

    # todo 需要提供一个错误页面
    raise e


def handle_user_exception(e):
    logger.exception('bizerror.')
    if 'api' in request.url:
        return FAIL(err_code=e.error_code, err_msg=e.error_remark)

    # todo 需要提供一个错误页面
    raise e


def init_app(app):
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(BizError, handle_user_exception)
