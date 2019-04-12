import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name": "youpingw.cn@gmail.com",
    "pass": "123456"}
).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
data = urllib.request.urlopen(req).read()
filehandle = open("./post.html", "wb")
filehandle.write(data)
filehandle.close()