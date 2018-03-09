from lxml import etree
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=fd1ac5ddfa8a48af93dea3f1257a7d82&p=8"
r = requests.get(url,headers=headers)
print(type(r.status_code))

html = etree.HTML(r.text)
lists = html.xpath('//div[@class="newlist_list_content"]/table[@class="newlist"]')
# lists=lists[1:]
for i in lists:
    pose = i.xpath('tr[1]/td[1]/div/a/@href')
    print(pose)















