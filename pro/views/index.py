import tornado.web
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        python_url = self.reverse_url("python_url")
        self.write('<a href="%s">hehe</a>' % python_url)


class IndexHandler2(RequestHandler):
    def initialize(self, word1):
        self.word1 = word1

    def get(self):
        self.write("<h1>Hello world!%s</h1>" % self.word1)

