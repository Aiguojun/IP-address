#coding:utf-8
import tornado.ioloop,tornado.httpserver
from tornado.web import RequestHandler
import tornado.web
import os,json
from tornado.web import asynchronous
from tornado.httpclient import AsyncHTTPClient

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')
class ShowHandler(RequestHandler):
    @asynchronous
    def get(self, *args, **kwargs):
        ip=self.get_query_argument('ip',None)
        if ip is not None:
            client=AsyncHTTPClient()
            client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s" % ip,callback=self.on_response)
        else:
            self.write('输入有误')
    def on_response(self,response):
            data=response.body
            datas=json.loads(data)
            print datas
            country=datas.get('country','')
            province=datas.get('province','')
            city=datas.get('city','')
            self.write('%s--%s--%s' % (country,province,city))
            self.finish()
if __name__=='__main__':
    app=tornado.web.Application([
        (r'/',IndexHandler),
        (r'/show',ShowHandler),
    ],
     template_path=os.path.join(os.path.dirname(__file__),'templates'),
     debug=True,
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()