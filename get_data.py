
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
import requests
from lxml import etree
from functools import reduce

def get_html(url):
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        return etree.HTML(r.text)
    else:
        print("具体职位页面请求失败！")
def get_data(html):
    data = dict()
    company_name = html.xpath('//div[@class="fixed-inner-box"]/div[1]/h2/a/text()')
    data["公司名称"] = company_name
    company_url = html.xpath('//div[@class="fixed-inner-box"]/div[1]/h2/a/@href')
    data["公司链接"] = company_url
    post_date = html.xpath('//ul[@class="terminal-ul clearfix"]/li[3]/strong/span/text()')
    data["提交日期"] = post_date
    job_requir_item = html.xpath('//div[@class="tab-inner-cont"]/p')
    # a = job_requir_item[4].xpath('text()')
    job_requir = []
    #下面的代码有点臃肿，此处应该
    for i in job_requir_item:
        j = i.xpath('text()')
        job_requir.append(j)
    job_requir = reduce(lambda x,y:x+y,job_requir)
    job_requir = [i.strip() for i in job_requir]
    job_requir = [i for i in job_requir if i]
    data["职位要求"] = job_requir
    job_local = html.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()')
    data["工作地点"] = job_local
    job_natua = html.xpath('//ul[@class="terminal-ul clearfix"]/li[4]/strong/text()')
    data["工作性质"] = job_natua
    job_experience = html.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()')
    data["工作经验"] = job_experience
    want_num = html.xpath('//ul[@class="terminal-ul clearfix"]/li[7]/strong/text()')
    data["招聘人数"] = want_num
    minimum_degree = html.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()')
    data["最低学历"] = minimum_degree
    welfares_item = html.xpath('//div[@class="inner-left fl"]/div[1]/span')
    welfares = []
    for i in welfares_item:
        welfare = i.xpath('text()')
        welfares.append(welfare)
    welfares = reduce(lambda x,y:x+y,welfares)
    data["福利"] = welfares
    job_name = html.xpath('//div[@class="inner-left fl"]/h1/text()')
    data["岗位名称"] = job_name
    salary = html.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()')
    data["薪水"] = salary
    job_category = html.xpath('//ul[@class="terminal-ul clearfix"]/li[8]/strong/a/text()')
    data["工作类别"] = job_category
    job_category_url = html.xpath('//ul[@class="terminal-ul clearfix"]/li[8]/strong/a/@href')
    data["岗位链接"] = job_category_url
    return data

if __name__ == '__main__':
    html = get_html("http://jobs.zhaopin.com/CC272558088J00110143501.htm?ssidkey=y&ss=409&ff=03&sg=58c01b8c215e46eb9fdcfd6d5ae4136d&so=1")
    data = get_data(html)
    print(data)


