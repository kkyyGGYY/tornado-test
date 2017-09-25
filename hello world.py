import tornado.web
# Tornado的基础web框架模块
import tornado.ioloop
# 核心io模块,封装了Linux的epoll和BSD的kqueue, 是tornado高效的基础


# 处理类，相当于Django中的类视图
class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    # 路由处理方法，(匹配后执行)
    def get(self):
        # 重写get方法
        """对应http的get请求方式"""
        self.write("Hello world!")


if __name__ == "__main__":
    # 创建了一个app实例（一个应用）
    # Application：web的一个核心类，是与服务器接口对应，里面保存了路由映射表，添加设置，用listen方法创建一个HTTP服务器实例，并绑定端口,此时服务器并没有开启监听
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # 绑定监听的端口，注意，此时也没有开启监听的端口
    app.listen(8899)
    # IOLoop.current()返回当前线程的IOLoop实例
    # IOLoop.start()：开启IOLoop实例的I/O循环，同时服务器开始监听
    tornado.ioloop.IOLoop.current().start()
