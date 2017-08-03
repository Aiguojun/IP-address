import re

from 多线程爬图 import picture

# url=r"http://588ku.com/beijing/0-0-pxnum-0-8-0-0-0-1/?h=bd&sem=1"
# url=r"http://588ku.com/banner/"
httpregex=re.compile("(http://\S*.jpg?)[\"|\!]",re.IGNORECASE)
for i in range(10):
    url=r"http://588ku.com/banner/0-0-pxnum-0-8-0-0-0-"+str(i)
    t= picture.getweb(url, httpregex)
    t.start()