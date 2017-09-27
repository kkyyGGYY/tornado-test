# coding=utf-8
import os
BASE_PATH = os.path.dirname(__file__)


options = {
    'port': 9900,
    # 'list': ['k', 'o', 'n', 'g', 'y', 'u']
}

# app的配置
settings = {
    'template_path': os.path.join(BASE_PATH, 'templates'),
    'static_path': os.path.join(BASE_PATH, 'statics'),
    # 'cookie_secret': '0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    # 'xsrf_cookies': False,
    'login_url': '/login',
    'debug': True,
}

# log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
