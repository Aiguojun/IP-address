#生成索引有序
class index:
    def __init__(self,path):
        self.openfile=open(path,"rb")
    def cerat(self):
        self.indexlist=[0]
        for line in self.openfile:
            self.indexlist.append(len(line))
        for i in range(len(self.indexlist)-2):
            self.indexlist[i+1]+=self.indexlist[i]

    def __del__(self):
        self.openfile.close()

path = r"F:\大数据相关数据\csdnsort.txt"
myindex = index(path)
myindex.cerat()
while True:
    linenum=eval(input("输入要查看哪一行"))
    myindex.openfile.seek(myindex.indexlist[linenum])
    line = myindex.openfile.readline()
    print(line.decode("gbk","ignore"))