#随机访问行，通过索引
class find:
    def __init__(self,path,indexpath):
        self.file=open(path,"rb")
        self.indexfile=open(indexpath,"rb")

    def doit(self,findstr,length):
        if findstr <= length:
            self.indexfile.seek(10*(findstr-1),0)
            getline=self.indexfile.read(10)
            getindex=eval(getline.decode("gbk","ignore"))
            self.file.seek(getindex)
            line=self.file.readline()
            line=line.decode("gbk","ignore")
            return line
        else:
            return "没有该行"
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
    length=getlength(t.file)
    print("文档一共有",length,"行")
    while True:
        findstr=eval(input("输入要查看的行"))
        print(t.doit(findstr,length))

main()