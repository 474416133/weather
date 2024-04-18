#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> response
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 17:12
@Desc   ：
"""
import math
from flask import jsonify


def create_response(err_msg, err_code, data):
    """
    response structure
    :param data: 数据
    :param err_msg: 错误信息
    :param err_code: 状态码，0表示正常，大于0表示有错误
    :return:
    """
    return {
        'err_code': err_code,
        'err_msg': err_msg,
        'data': data
    }


def create_pagination(records, total, page_size, page_no):
    """
    返回分页信息
    :param records: 结果集
    :param total: 记录总数
    :param page_size: 每页记录数
    :param page_no: 页数
    :return:
    """
    total_page = math.ceil(total/ page_no * page_size)
    return {
        'records': records,
        'total': total,
        'page_size': page_size,
        'page_no': page_no,
        'total_page': 0,
        'has_next': page_no < total_page
    }


def OK(data, err_msg='OK', err_code=0):
    return jsonify(**create_response(err_msg, err_code, data))


def FAIL(err_code, err_msg='ERROR', data=None):
    return jsonify(**create_response(err_msg, err_code, data))


def page(records, total, page_size, page_no):
    return OK(create_pagination(records, total, page_size, page_no))


