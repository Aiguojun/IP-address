#二分法第一步必须排序
import time
openfile=open(r"F:\大数据相关数据\csdn.txt","rb")
savefile=open(r"F:\大数据相关数据\csdnsort.txt","wb")

linelist=openfile.readlines()
openfile.close()

def getuser(line):
    line=line.decode("gbk","ignore")
    userlist=line.split(" # ")
    return userlist[0]
linelist.sort(key=lambda x:getuser(x))
for line in linelist:
    savefile.write(line)
savefile.close()
