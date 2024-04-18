#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> http
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/17 16:51
@Desc   ：
"""
import logging
import urllib
import requests
from requests.auth import AuthBase


logger = logging.getLogger('requests')


class TianqiAuthBase(AuthBase):
    """
    天气授权
    """

    def __init__(self, app_id, app_secret, version='v63', unescape=1, verify=False):
        """

        :param app_id:
        :param app_secret:
        :param verify:
        """
        self._app_id = app_id
        self._app_secret = app_secret
        self._version = version
        self._unescape = unescape
        self._verify = verify
        self._query = self.build_query()


    def __call__(self, request):
        """
        @override
        :param request:
        :return:
        """
        if '?' in request.url:
            request.url = request.url + '&' + self._query
        else:
            request.url = request.url + '?' + self._query
        return request

    def build_query(self):

        return urllib.parse.urlencode({
            'appid': self._app_id,
            'appsecret': self._app_secret,
            'version': self._version,
            'unescape': self._unescape
        })


def default_auth(client):
    """
    :param client:
    :return:
    """

    return TianqiAuthBase(client.kwargs.get('app_id'),
                          client.kwargs.get('app_secret'))



class APIRequestError(RuntimeError):

    def __init__(self, resp):
        self.resp = resp
        self.req = resp.request

    def __str__(self):
        return '[request] url: {}, method:{}, headers: {}, params: {}, data:{}, json:{};' \
               '[response] status_code: {}, content: {}'.format(self.req.url,
                                                                self.req.method,
                                                                self.req.headers,
                                                                self.req.params,
                                                                self.req.data,
                                                                self.req.json,
                                                                self.resp.status_code,
                                                                self.resp.content)



class APIClient(object):
    """

    """
    def __init__(self, host, verify=False, make_auth=default_auth, **kwargs):
        """

        :param host:
        """
        self.kwargs = kwargs
        self._host = host
        self._make_auth = make_auth
        self._verify = verify
        self._auth = None

        self._session = requests.Session()
        if callable(self._make_auth):
            self._auth = self._make_auth(self)
            self._session.auth = self._auth


    def execute(self, method, path, **kwargs):
        """
        :param method:
        :param path:
        :param kwargs:
            - params:
            - data:
            - headers:
            - cookies:
            - files:
            - auth:
            - timeout:
            - allow_redirects:
            - proxies:
            - hooks:
            - stream:
            - verify:
            - cert:
            - json:
        :return:
        """
        uri = f'{self._host}{path}'
        kwargs.update(verify=self._verify)
        resp = self._session.request(method, uri, **kwargs)
        if resp.status_code > 400:
            logger.warning('uri: {}, method: {}, kwargs: {},'
                           ' status_code: {}, resp_text: {}'.format(uri,
                                                                    method,
                                                                    kwargs,
                                                                    resp.status_code,
                                                                    resp.content))
            raise APIRequestError(resp)
        elif resp.status_code < 300:
            return resp.json()
        return resp

    def get(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('get', path, **kwargs)

    def post(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('post', path, **kwargs)

    def put(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('put', path, **kwargs)

    def delete(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('delete', path, **kwargs)

    def patch(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('patch', path, **kwargs)

    def head(self, path, **kwargs):
        """
        :param path:
        :param kwargs:
        :return:
        """
        return self.execute('head', path, **kwargs)

    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()