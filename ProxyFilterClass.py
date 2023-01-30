import threading as thr
import numpy as np
import requests 
from bs4 import BeautifulSoup 


class ProxyFilterAPI(object): # From  https://free-proxy-list.net/ 
    Yes = 'yes'
    No = 'no'

    def __init__(self) -> None:
        self.Threads = []  # List Of Threads that is Working
        self.Errors = []  # Errors in https request 
        self.ProxiesList = [] # Good Proxies

    def getFreshProxyList(
        self,
        httpsFilter:str ,
        ExportToTXT:bool= False ,
        ):
        ProxyList = []
        response = requests.get(url = 'https://free-proxy-list.net/')
        self.soup = BeautifulSoup(response.text,'html.parser')
        table = self.soup.find("tbody")
        rows = table.find_all("tr")
        for row in rows :
            row = row.find_all('td')
            ip = row[0].text
            port = row[1].text
            https = row[6].text
            #print(f"{ip}:{port} --> https:{https}")
            if https == httpsFilter :
                ip_port = f"{ip}:{port}"
                ProxyList.append(ip_port)
        if ExportToTXT == True :
            with open("Proxies.txt",'w+')as file :
                file.writelines([ip_port+"\n" for ip_port in ProxyList])
                file.close()
        return ProxyList


    def testProxy(self,ip_port):
        proxy = {'http':ip_port,'https':ip_port}
        try:
            response = requests.get(url = "http://httpbin.org/ip",proxies= proxy ,timeout = 5)
            self.ProxiesList.append(ip_port)
        except Exception as e :
            self.Errors.append(e)


    def threadingRequstFilter(self,ip_portLists):
        for iplist in ip_portLists:
            task = thr.Thread(target = self.testProxy,args = (iplist,))
            self.Threads.append(task)
            task.start()

    def wait(self)-> None:
        for task in self.Threads:
            if task.is_alive() :
                task.join()

    def autoAPI(self,wait:bool= True):
        firstlist = self.getFreshProxyList(httpsFilter=self.Yes)
        self.threadingRequstFilter(firstlist)
        if wait == True :
            self.wait()
        return self.ProxiesList
        

        
