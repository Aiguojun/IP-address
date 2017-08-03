import urllib
import urllib.request
import re
import storagepicture
import threading
class getweb(threading.Thread):
    def __init__(self,starturl,regex):
        threading.Thread.__init__(self)
        self.starturl=starturl
        self.pat=regex
    def run(self):
        mystr=urllib.request.urlopen(self.starturl).read()
        mystr=mystr.decode("utf-8")
        mylist=self.pat.findall(mystr)
        storagepicture.load(mylist)


# url=r"http://588ku.com/beijing/0-0-pxnum-0-8-0-0-0-1/?h=bd&sem=1"
# url=r"http://588ku.com/banner/"
# httpregex=re.compile("(http://\S*.jpg?)[\"|\!]",re.IGNORECASE)
# for i in range(10):
#     url=r"http://588ku.com/banner/0-0-pxnum-0-8-0-0-0-"+str(i)
#     t=picture.getweb(url,httpregex)
#     t.run()