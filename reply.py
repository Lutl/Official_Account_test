# -*- coding:utf-8 -*-
import time


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict["ToUserName"] = toUserName
        self.__dict["FromUserName"] = fromUserName
        self.__dict["CreateTime"] = int(time.time())
        # 因为receive文件种将unicode转换为了bytes类型，输出返回时要再转换回去
        self.__dict["Content"] = content.decode("utf-8")

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
        """
        print(XmlForm.format(**self.__dict))
        return XmlForm.format(**self.__dict)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = toUserName
        self.__dict["FromUserName"] = fromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = mediaId
    
    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                    <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
        """
        print(XmlForm.format(**self.__dict))
        return XmlForm.format(**self.__dict)
