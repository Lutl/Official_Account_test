# -*- coding:utf-8 -*-
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

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
