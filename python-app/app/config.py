import os

class BaseConfig(object):
    APP_NAME = 'pythonscraping'
    LOGO = 'https://via.placeholder.com/50'
    SECRET_KEY = 'x-python-scraing-key'
    SECRET_KEY_HASH = 'KuQmvnxXEjR7KXwfucgerTf6YwZV5Amz5awwxf5PFgkpGrb3Jn'
    GET_QUERY_LIMIT = 10

    LOG_LEVEL = 'DEBUG'


class LocalConfig(BaseConfig):
    LOG_LEVEL = 'DEBUG'


class DevConfig(BaseConfig):
    LOG_LEVEL = 'DEBUG'


class ProdConfig(BaseConfig):
    LOG_LEVEL = 'INFO'

