import requests
from lxml import etree
import time
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
#获取代理Ip网页的网页源代码
def get_html(url):
    try:
        r = requests.get(url,headers=headers)
        if r.status_code == 200:
            html = etree.HTML(r.text)
            print("IP获取任务中获取html成功！")
            return html
        else:
            print("响应码异常！")
    except:
        print("网络请求异常！")
#快代理需要设置请求时间间隔，过快会导致下一个请求返回503状态码
def get_kuaidaili(page):
    ip_data = {"http":[],"https":[]}
    for i in range(1,page+1):
        url = "https://www.kuaidaili.com/free/inha/%d/"%i
        time.sleep(1)
        html = get_html(url)
        tds = html.xpath('//tbody/tr')
        for td in tds:
            ip = td.xpath('td[1]/text()')[0]
            ip_mode = td.xpath('td[4]/text()')[0]
            if ip_mode == "HTTP":
                ip_data["http"].append(ip)
            elif ip_mode == "HTTPS":
                ip_data["https"].append(ip)

    return ip_data
def data_into_txt(ip_data):
    f= open("ip_list_http.txt","w")
    if ip_data["http"]:
        for i in ip_data["http"]:
            f.write(i+"\n")
    g = open("ip_https_list.txt","w")
    if ip_data["https"]:
        for i in ip_data["https"]:
            f.write(i+"\n")
    g.close()
    f.close()
#用于验证ip的url
#http://icanhazip.com/
#http://pv.sohu.com/cityjson?ie=utf-8
def vali_1_ip(valiurl):
    # url = "http://icanhazip.com/"
    valid_ip = []
    f=open("ip_list_http.txt","r")
    while True:
        ip = f.readline().strip()
        if ip:
            proxies={"http":"http://"+ip}
            print(proxies)
            try:
                r = requests.get(valiurl,headers=headers,proxies = proxies,timeout = 5)
                print("正在验证的ip是：",ip)
                print(r.text)
                valid_ip.append(ip)
                return valid_ip
            except:
                print("该IP请求异常,无效！")
        else:
            break
def valid_ip_intotxt(vaild_ip_data):
    f = open("valid_ip.txt","w")
    for i in vaild_ip_data:
        f.write(i+"\n")
    f.close()

if __name__ == '__main__':
    # get_html("https://www.kuaidaili.com/free/inha/2/")
    # ip = get_kuaidaili(5)
    # data_into_txt(ip)
    # vali_1_ip("http://icanhazip.com/")
    pass



