import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # app.listen(8899)
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()

