#源文件不排序生成索引
class index:
    def __init__(self,path,savepath):
        self.file=open(path,"rb")
        self.savefile=open(savepath,"wb")
    def getuser(self,x):
        self.file.seek(x)
        line=self.file.readline()
        line=line.decode("gbk","ignore")
        linelist=line.split(" # ")
        user=linelist[0]
        return user
    def dosort(self):
        lengthlist=[0]
        for line in self.file:
            lengthlist.append(len(line))
        for k in range(len(lengthlist)-1):
            lengthlist[k + 1] += lengthlist[k]
        lengthlist.sort(key=lambda x:self.getuser(x))
        return  lengthlist
    def creatindex(self):
        indexlist=self.dosort()
        print("排序完成")
        return indexlist
    def write(self):
        for i in self.creatindex():
            self.savefile.write(format(i,"10d").encode("utf-8","ignore"))
    def __del__(self):
        self.savefile.close()
        self.file.close()

def main():
    path = r"F:\大数据相关数据\csdn.txt"
    savepath = r"F:\大数据相关数据\index-csdn.txt"
    t=index(path,savepath)
    t.write()

main()