# -*- coding:utf-8 -*-

import hashlib
import web

import reply
import receive

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
            for i in list:
                sha1.update(i.encode('utf-8'))  # hashlib转换字符串不能使用unicode格式
            hashcode = sha1.hexdigest()
            print("handle/Get func: hashcode({}), signature:({})".format(hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        # TODO: python2.7的语法可能存在问题
        except Exception as Argument:
            return Argument
    

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is {}".format(webData))
            recMsg = receive.parse_xml(webData)
            # 使用isinstance判断类所属关系
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == "text":
                    content = recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == "image":
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂不处理")
                return reply.Msg().send()
        except Exception as Argument:
            return Argument
