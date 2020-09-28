# -*- coding:utf-8 -*-
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


if __name__ == '__main__':
    # app = web.application(urls, globals())
    # TODO: 需要解决默认使用8080端口启动项目的问题
    app = MyApplication(urls, globals())
    app.run(port=80)

# import web

# urls = (
#     '/(.*)', 'hello'
# )
# app = web.application(urls, globals())

# class hello:
#     def GET(self, name):
#         if not name:
#             name = 'World'
#         return 'Hello, ' + name + '!'

# if __name__ == "__main__":
#     app.run()
