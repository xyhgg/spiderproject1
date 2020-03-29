import requests
from requests.exceptions import RequestException
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 ',
}

name = input('请输入要爬取的图书信息:')
sum = int(input('请输入要爬取的图书的总页数:'))
# 1.准备url
url = 'http://search.dangdang.com/?key={}&act=input'.format(name)
start = 1
while start <= sum:
    print('正爬取第' + str(start) + '页信息')
    start += 1
    # 2.发送请求获取数据
    response = requests.get(url)

    # 3.获取html字符串
    strs = response.text

    # 4.获取element对象
    element = html.fromstring(strs)

    # 5.先获取分类
    li_list = element.xpath('//div[@id="search_nature_rg"]/ul/li')

    # 6.再获取数据
    for li in li_list:
        book_name = li.xpath("./a/@title")[0]
        book_link = li.xpath("./a/@href")[0]
        book_price = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')
        if not book_price:
            book_price = li.xpath('./div[@class="ebook_buy"]/p[@class="price e_price"]//text()')
        if not book_price:
            book_price = ['没有价格']

        book_writer = li.xpath('./p[@class="search_book_author"]/span/a//text()')
        if not book_writer:
            book_writer = ['未知作者']

        book_publishtime = li.xpath('./p[@class="search_book_author"]/span/following-sibling::span//text()')
        if not book_publishtime:
            book_publishtime = ['未知出版时间']

        book_publish = li.xpath('./p[@class="search_book_author"]/span/following-sibling::span/following-sibling'
                                '::span/a//text()')
        if not book_publish:
            book_publish = ['未知出版社']

        if len(li.xpath("./a/img/@*")) == 2:
            book_photo = li.xpath("./a/img/@src")[0]
        else:
            book_photo = li.xpath("./a/img/@data-original")[0]

        book_comment = li.xpath('./p[@class="search_star_line"]/a//text()')
        if not book_comment:
            book_comment = ['0条评论']

        book_detail = li.xpath('./p[@class="detail"]//text()')
        if not book_detail:
            book_detail = ['暂无简介']

        with open('book.txt', 'a', encoding='utf8') as f:
            f.write(book_name.strip() + "\n" + book_link + "\n" + book_price[0] + "\n" + book_writer[0] + "\n" +
                    book_publishtime[0].strip().lstrip('/') + "\n" + book_publish[0] + "\n" + book_photo + "\n" +
                    book_comment[0] + "\n" + book_detail[0] + "\n\n"
                    )

    try:
        # 爬取下一页
        a_url = element.xpath('//li[@class="next"]/a/@href')[0]
        url = 'http://search.dangdang.com' + a_url
    except:
        print('完成，共爬取了' + str(start - 1) + '页,请在book.txt中查看')
        break
