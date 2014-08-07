# -*- coding: utf-8 -*-
'''#行业短信测试及结果收集
'''
import os
import urllib.parse, urllib.request, http.cookiejar

"""cookie"""
cookiefile = os.getcwd()+"\cookie.txt"
cookie=http.cookiejar.LWPCookieJar()
if os.path.exists(cookiefile): cookie.load(cookiefile,True,True)
chandle=urllib.request.HTTPCookieProcessor(cookie)
"""获取数据"""
def getData(url):

    r=urllib.request.Request(url)
    r.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)')
    r.add_header('Content-Type', 'application/x-www-form-urlencoded')
    r.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')	
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    chandle.cookiejar.save(cookiefile,True,True)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data
def postData(url,data):
    data=urllib.parse.urlencode(data);data=bytes(data,'utf-8')
    r=urllib.request.Request(url,data)
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    chandle.cookiejar.save(cookiefile,True,True)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data


if __name__ == "main":
    print("test")
    os.system("pause  &cls")

