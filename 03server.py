import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(8000)
    httpServer.start(5)

    tornado.ioloop.IOLoop.current().start()

