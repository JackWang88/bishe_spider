import urllib.request
keywd="石头老师"
keywd_quote = urllib.request.quote(keywd)
url="http://www.baidu.com/s?wd="+keywd_quote
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("./get_baidu_search.html","wb")
fhandle.write(data)
fhandle.close()


