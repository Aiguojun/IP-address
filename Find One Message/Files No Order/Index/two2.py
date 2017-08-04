#通多索引查找内容，此时源文件没有任何操作（无排序）
#hight的数值需要传入，此时没法获取
import time
class anyfind:
    def __init__(self,path,indexpath):
        self.file=open(path,"rb")
        self.indexfile=open(indexpath,"rb")
    def serach(self,findstr):
        low=0
        high=6428632-1
        while low <= high :
            mid=(low+high)//2
            self.indexfile.seek(10*mid,0)
            indexline=self.indexfile.read(10)
            indexnumber=eval(indexline.decode("gbk",errors="ignore"))
            self.file.seek(indexnumber)
            line=self.file.readline()
            line=line.decode("gbk","ignore")
            linelist=line.split(" # ")
            middata=linelist[0]
            if findstr < middata:
                high=mid-1
            elif findstr > middata:
                low=mid+1
            else:
                print("找到了",mid,line)
                break

def main():
    path = r"F:\大数据相关数据\csdn.txt"
    indexpath = r"F:\大数据相关数据\index-csdn.txt"
    t=anyfind(path,indexpath)
    while True:
        findstr=input("输入要查找的内容")
        start=time.time()
        t.serach(findstr)
        end=time.time()
        print("一共用时",end-start)

main()