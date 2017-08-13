#coding:utf-8
import tornado.web
import tornado.ioloop
from tornado.websocket import WebSocketHandler
import tornado.httpserver
import config,datetime


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html')
class ChatHandler(WebSocketHandler):
    users=set()
    def open(self, *args, **kwargs):
        self.users.add(self)
        for user in self.users:
            ip=self.request.remote_ip
            now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message=u'[%s]---[%s]---得道成仙'% (ip,now)
            user.write_message(message)
    def on_message(self, message):
        for user in self.users:
            ip=self.request.remote_ip
            now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.write_message('[%s]---[%s]-:%s' % (ip,now,message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            ip=self.request.remote_ip
            now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.write_message('[%s]--[%s]--堕落凡尘' % (ip,now))

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[(r'/',IndexHandler),(r'/chat',ChatHandler)]
        settings=config.settings
        super(Application,self).__init__(handlers,**settings)
if __name__=="__main__":
    app=Application()
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(config.port,'0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
