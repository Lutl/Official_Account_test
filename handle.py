# -*- coding:utf-8 -*-

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "Lxhv2vkQJVHy4OqY7g8c0L66GzS7TJ2H"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/Get func: hashcode({}), signature:({})".format(hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        # TODO: python2.7的语法可能存在问题
        except Exception as Argument:
            return Argument