import tornado.web
import config
from tornado.web import url
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            # (r'/kong', index.IndexHandler2, {'word1': 'good'}),
            url(r'/yu', index.IndexHandler2, {'word1': 'nice'}, name='python_url'),
        ]
        super(Application, self).__init__(handlers, **config.settings)
