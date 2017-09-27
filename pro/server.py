import config
import tornado.web
import tornado.httpserver
import tornado.ioloop
from views import index


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", index.IndexHandler),
    ], **config.settings)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(config.options['port'])
    tornado.ioloop.IOLoop.current().start()
