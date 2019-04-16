import urllib.request
import urllib.parse
import time

# 本函数功能为爬取链接raw_url的第 begin 页至 end页，时间延迟为timeout，以raw_filename作为文件名保存
def get_webpage(raw_url, raw_filename, begin, end, timeout):
    #模拟成浏览器
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)

    # 请求page次网页
    for i in range(begin, end + 1):
        full_url = raw_url + str(i) + ".html"
        full_filename = raw_filename + str(i) + ".html"
        file = urllib.request.urlopen(full_url)
        data = file.read().decode('UTF-8')

        # 将网页写入文件
        fileHandle = open(full_filename, 'w', encoding='UTF-8')
        fileHandle.write(data)
        fileHandle.close()
        time.sleep(timeout)  # 每次请求后等待timeout秒，减轻服务器压力
    return 0


爬虫爬取路线
# 1.获取全世界的合法网站列表
raw_url = "http://alexa.chinaz.com/Global/index_"
raw_filename = "./webpage/legal_webpage/global_legal_website_list_"
因为全世界的合法网站列表第一个链接为index.html,所以下面的调用从页面2开始
get_webpage(raw_url, raw_filename, 2, 20, 3)

# 2.获取中国的合法网站列表
raw_url = "http://alexa.chinaz.com/Country/index_CN_"
raw_filename = "./webpage/legal_webpage/china_legal_website_list_"
get_webpage(raw_url, raw_filename, 1, 20, 3)

# 3.获取全世界的钓鱼网站列表
raw_url = "http://www.phishtank.com/phish_archive.php?page="
raw_filename = "./webpage/phish_webpage/phish_website_webpage_"
get_webpage(raw_url, raw_filename, 1, 1000, 3)




