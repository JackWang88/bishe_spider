# bishe_spider
UPDATE：2019.4.12 10.43 
The main work of this project is: 
1. Crawl the list of top-ranked websites in the world and the country on alexa and the list of recent phishing websites on  www.phishtank.com 
2. Crawl the DNS, whois and SSL information of the website in 1 
3. Train the second classification model of a legitimate website and phishing website with the information in 1, 2 
4. Use the model in 3 to determine if the unknown website is a phishing website.
本项目的主要工作为： 
1.爬取alexa上全世界和全国排名靠前的网站URL列表和 www.phishtank.com 上近期的钓鱼网站URL列表 
2.爬取1中网站的DNS、whois和SSL信息 
3.以1，2中的信息训练一个合法网站和钓鱼网站的二分类模型 
4.使用3中的模型判断未知网站是否为钓鱼网站
