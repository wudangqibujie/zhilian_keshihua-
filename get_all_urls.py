city_url = {"深圳":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=58c01b8c215e46eb9fdcfd6d5ae4136d&p=",
            "北京":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&isadv=0&sg=a08e980940e348b39b60e740a33ee014&p=",
            "上海":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&isadv=0&sg=a805c1f2e35647cd9edb0db3554df18f&p=",
            "广州":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=python&isadv=0&sg=c4c441a887954acd893effb705944e31&p=",
            "天津":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%A4%A9%E6%B4%A5&kw=python&isadv=0&sg=0c8ba7dc49b04469920e858ccecf1614&p=",
            "武汉":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&kw=python&isadv=0&sg=a3549b6cbf1847f098a4618dd5c1c253&p=",
            "西安":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E8%A5%BF%E5%AE%89&kw=python&isadv=0&sg=0e73cccd6708407e8474038dc76f3055&p=",
            "成都":"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=python&isadv=0&sg=adaa89c8e37d4d7c9bc10e220bf587de&p="
            }
import requests
import re
from lxml import etree
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
#下面是为了获取每个城市页面下的最大页数
def get_max_page_urls(city_url):
    r = requests.get(city_url,headers=headers)
    if r.status_code == 200:
        html = etree.HTML(r.text)
        max = html.xpath('//div[@class="pagesDown"]/ul/li[@class="nextpagego-box"]/button/@onclick')
        print(max)
        pattern = re.compile("value,(.*?),")
        max_num = re.findall(pattern,max[0])[0]
        return int(max_num)
    else:
        print("请求城市页面失败！")
#是获取城市的页面下的所有职位列表URL
def get_item_urls(city_url):
    r = requests.get(city_url,headers=headers)
    if r.status_code == 200:
        html = etree.HTML(r.text)
        item_url = html.xpath('//div[@class="newlist_list_content"]/table[@class="newlist"]')
        pose_urls = []
        for i in item_url[1:]:
            pose_url = i.xpath('tr[1]/td[1]/div/a[1]/@href')
            pose_urls.append(pose_url[0])
        return pose_urls
    else:
        print("抓取职位url失败了！")
if __name__ == '__main__':

    # for key,value in city_url.items():
    #     max_num = get_max_page_urls(value)
    #     print("%s的最大页码是：%d"%(key,max_num))

    # a=get_item_urls(city_url["深圳"]+"1")
    # print(a)


    pass




