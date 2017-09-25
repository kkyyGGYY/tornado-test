import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# tornado.options.define(name=None,default=None,type=None,help=None,metavar=None,multiple=False,group=None,callback=None)
tornado.options.define('port', default=8000, type=int, help='this is the PORT', multiple=False)
tornado.options.define('list', default=[], type=str, help='this is the List', multiple=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    print(tornado.options.options.port, tornado.options.options.list)
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
