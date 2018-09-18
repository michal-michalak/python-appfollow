from __future__ import unicode_literals

from requests import RequestException

__all__ = [
    'AppFollowAPIException', 'AppFollowAPIBadRequest',
    'AppFollowAPIBadGateway', 'AppFollowAPIGatewayTimeout'
]


class AppFollowAPIException(RequestException):
    pass


class AppFollowAPIBadRequest(AppFollowAPIException):
    pass


class AppFollowAPIBadGateway(AppFollowAPIException):
    pass


class AppFollowAPIGatewayTimeout(AppFollowAPIException):
    pass
