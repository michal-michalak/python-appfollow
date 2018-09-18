import hashlib
import requests

from collections import OrderedDict

from .exceptions import *


class AppFollowAPI:
    def __init__(self, cid, api_secret):
        self.base_url = 'http://api.appfollow.io'
        self.cid = cid
        self.api_secret = api_secret
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def _sign(self, path, params=None):
        params = params or {}
        params['cid'] = self.cid
        params = OrderedDict(sorted(params.items()))
        params_str = ''.join([f'{key}={value}' for key, value in params.items()])
        s = params_str + path + self.api_secret
        return hashlib.md5(s.encode('utf-8')).hexdigest()

    def _make_request(self, method, path, **kwargs):
        params = kwargs.pop('params', {})
        sign = self._sign(path, params)
        params.update({'sign': sign})
        kwargs.update({'params': params})
        url = self.base_url + path
        response = requests.request(method, url, **kwargs)

        # https://appfollow.docs.apiary.io/#introduction/handling-errors
        if response.ok:
            payload = response.json()
            if 'error' in payload:
                raise AppFollowAPIBadRequest(response=response)
            else:
                return payload
        if response.status_code == 502:
            raise AppFollowAPIBadGateway(response=response)
        if response.status_code == 504:
            raise AppFollowAPIGatewayTimeout(response=response)

    def get_ratings(self, ext_id):
        return self._make_request('GET', '/ratings', params={'ext_id': ext_id})

    def get_reviews(self, ext_id):
        return self._make_request('GET', '/reviews', params={'ext_id': ext_id})

    def get_versions(self, ext_id):
        return self._make_request('GET', '/versions', params={'ext_id': ext_id})
