#生成索引的文件
class indexfind:
    def __init__(self,path,indexpath):
        self.file=open(path,"rb")
        self.indexfile=open(indexpath,"wb")
    def create(self):
        lengthlist=[0]
        for line in self.file:
            lengthlist.append(len(line))
        print("lengthlist完成")
        for i in range(len(lengthlist)-2):
            lengthlist[i+1]+=lengthlist[i]
        print("索引完成")
        for k in lengthlist:
            self.indexfile.write(format(k,"10d").encode("utf-8","ignore"))
        print("写入完成")
    def __del__(self):
        self.indexfile.close()
        self.file.close()

def main():
    path= r"F:\大数据相关数据\csdnsort.txt"
    indexpath= r"F:\大数据相关数据\index-csdn-sort.txt"
    t=indexfind(path,indexpath)
    t.create()
    print("完成")

main()