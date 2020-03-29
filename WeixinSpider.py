from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError

base_url = 'https://weixin.sogou.com/weixin?'
keyword = '风景'
headers = {
    'Cookie': 'IPLOC=CN4111; SUID=E0EF78B66920A00A000000005E7EC412; SUV=1585366033707741; ABTEST=0|1585366036|v1; weixinIndexVisited=1; JSESSIONID=aaaoI-nVSE-rl-K2H_uex; ppinf=5|1585366394|1586575994|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozOmdoYnxjcnQ6MTA6MTU4NTM2NjM5NHxyZWZuaWNrOjM6Z2hifHVzZXJpZDo0NDpvOXQybHVIa255LXhka1ZYZl96akV1clQ2NzZrQHdlaXhpbi5zb2h1LmNvbXw; pprdig=l0RK9JF02xVQuwcEgCSJarzOY2-iOvlJyzndY5fWnBTfMVgGuuwHiVviIUAtxyzF4Ylzqe0Qsr9R7ofbV7ezSrk4AYYUtKrqb9EiBLsPZO7nqzuFLD6X-ZwF3LDOG79H2dFwyxDujQ95vmNA6ISb-Hcxr--uGqSpEAPmuJb6v6o; sgid=00-51973167-AV5ibxXpU2tz4WasJmfd3LVM; ppmdig=15853799490000004d84b00ed025116c3035b99291d8dc1c; PHPSESSID=rnp6m0pdvg8dvpon9s9m7ce5m2; SNUID=3F31A668DEDB7F3ACF005EADDF0181C5; successCount=1|Sat, 28 Mar 2020 07:26:42 GMT; sct=2',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # need proxy
            print('302')
    except ConnectionError:
        return get_html(url)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        print(html)


if __name__ == '__main__':
    main()
