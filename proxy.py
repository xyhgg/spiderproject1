import requests
from requests import ReadTimeout

proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'http://httpbin.org/get'


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    try:
        response = requests.get(url, proxies=proxies)
        print('成功请求的代理IP', proxy)
        return response.text
    except Exception as e:   # 可以捕获除与程序退出sys.exit()相关之外的所有异常
        return crawl(target_url, get_random_proxy())
    # except requests.exceptions.ProxyError:
    #     return crawl(target_url, get_random_proxy())
    # except ReadTimeout:
    #     return crawl(target_url, get_random_proxy())
    # except requests.exceptions.ConnectTimeout:
    #     return crawl(target_url, get_random_proxy())


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = get_random_proxy()
    print('第一个尝试请求的代理IP', proxy)
    html = crawl(target_url, proxy)
    print(html)


if __name__ == '__main__':
    main()
