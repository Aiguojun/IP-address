#通过索引查找文件，找出要查找的内容
import time
class find:
    def __init__(self,path,indexpath):
        self.file=open(path,"rb")
        self.indexfile=open(indexpath,"rb")
    def doit(self,findstr,hight):
        low=0
        #此处的hight是文件的行数
        hight=hight-1
        while low <= hight:#从0开始索引，所以比行数少一
            mid=(low+hight)//2
            self.indexfile.seek(10*mid,0)
            line=self.indexfile.read(10)
            userindex=eval(line.decode("gbk","ignire"))
            self.file.seek(userindex)
            getline=self.file.readline()
            getline=getline.decode("gbk","ignore")
            userlist=getline.split(" # ")
            middata=userlist[0]
            if findstr < middata:
                hight=mid-1
            elif findstr > middata:
                low=mid+1
            else:
                print("找到了",mid,getline)
                break
    def __del__(self):
        self.indexfile.close()
        self.file.close()
def getlength(file):
    i=0
    for line in file:
        i+=1
    return i
def main():
    path=r"F:\大数据相关数据\csdnsort.txt"
    indexpath=r"F:\大数据相关数据\index-csdn-sort.txt"
    t=find(path,indexpath)
    hight = getlength(t.file)
    while True:
        findstr=(input("输入要查找的内容"))
        start = time.time()
        t.doit(findstr,hight)
        end = time.time()
        print("一共用时",end - start)
main()
