import tornado.web
import tornado.ioloop
import tornado.httpserver
import config


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")


if __name__ == "__main__":
    print(config.options['list'])
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], **config.settings)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(config.options['port'])

    tornado.ioloop.IOLoop.current().start()
