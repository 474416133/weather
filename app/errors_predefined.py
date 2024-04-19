#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> errors_predefined
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/18 22:35
@Desc   ：
"""

from app.common.errors import IError


class ERROR(IError):
    TA_API_INVOKE_ERROR = 3000 # 错误码