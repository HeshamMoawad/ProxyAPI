import requests
import threading
import numpy as np

url = "https://httpbin.org/ip"


headers = {
    'accept': 'application/json',
    'accept-encoding':'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://httpbin.org/',
    'sec-ch-ua':' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# with open('proxies.txt','r') as file :
#     proxylist = [proxy.replace("\n","") for proxy in file.readlines()]
#     #print(proxylist)

# Allgood = []

# def ProxyFilter(proxylist):
#     for ip_port in proxylist:
        
#         proxy ={
#             'http': f'https://{ip_port}' ,
#             'https': f'https://{ip_port}' ,
#         }
#         session = requests.Session()
#         session.proxies = proxy
#         try: 
#             res = session.get(url,timeout=5)#,headers
#             print(res)
#             if res.status_code == 200 :
#                 Allgood.append(proxy)
#                 print(f"There are proxy good -> {proxy}")
#         except Exception as e :
#             #print(e)
#             pass
    

# tasks = []
# proxylists = np.array_split(proxylist,100)

# for prolist in proxylists:
#     task1 = threading.Thread(target=ProxyFilter,args=(prolist,))
#     task1.start()
#     tasks.append(task1)

# for task2 in tasks:
#     task2.join()
# print(f"\nAll Good Proxies -> {Allgood}\n")
# print("Ended")



# proxy = {
#     'http': 'https://41.33.47.147:1981', 
#     'https': 'https://41.33.47.147:1981'
#     }


#         proxy ={
#             'http': f'https://{ip_port}' ,
#             'https': f'https://{ip_port}' ,
#         }
session = requests.Session()
#session.proxies = proxy
#         try: 
res = session.get(url,timeout=5)
print(res.json())
#             print(res)
#             if res.status_code == 200 :
#                 Allgood.append(proxy)
#                 print(f"There are proxy good -> {proxy}")
#         except Exception as e :
#             #print(e)
#             pass




