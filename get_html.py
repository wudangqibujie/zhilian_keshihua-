import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
proxies=None
ip="http://127.0.0.1"
def ip_daili(ip):
    def deco(func):
        def wrapper(url):
            global proxies
            proxies = {"http":ip}
            return func(url)
        return wrapper
    return deco

@ip_daili(ip)
def common_get(url):
    # r = requests.get(url,headers=headers,proxies = proxies)
    print(proxies)

if __name__ == '__main__':
    common_get("as")
