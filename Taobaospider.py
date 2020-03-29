import requests
from requests.exceptions import RequestException
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 ',
    'cookie': 'thw=cn; v=0; cookie2=1d713b427ccacb6430d829c64957eac6; t=b7d00b1f013af827800b1fb56b4cb4d6; '
              '_tb_token_=55e0361335b7b; cna=AY8AF3n8+BcCAbZ47aQPAaVk; _samesite_flag_=true; '
              '_m_h5_tk=0a581e644ce7a5ae719cd14c1b918436_1585207669660; _m_h5_tk_enc=880c81918474fcd5d92ea7cb75a9965a; '
              'sgcookie=ENhskOSFHJkUmjRiMLrtj; unb=2995190186; '
              'uc3=id2=UUGrc1b%2FlxaPFA%3D%3D&nk2=BJ6EfZW0&vt3=F8dBxd9hhEkmsQ4ZANI%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; '
              'csg=9775c7ab; lgc=ghbgjb; cookie17=UUGrc1b%2FlxaPFA%3D%3D; dnk=ghbgjb; skt=7ca9a1294d6efd0f; '
              'existShop=MTU4NTIwMDc2OQ%3D%3D; '
              'uc4=id4=0%40U2OcQ9RNAzOh%2FP0xljXS9MlHBDxr&nk4=0%40BprSdY3UOFd7bvJB0XeJRRU%3D; tracknick=ghbgjb; '
              '_cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=b65; _nk_=ghbgjb; '
              'cookie1=B0ADe6%2Fcz4HYeWH2TA%2F2jd01WEq2WWaABpyPKeD2ncI%3D; '
              'tfstk=cLpABROXT40cQOZ_YDclC-A_py1AawM1SoQ3BcOXo7G7My2TCsYMKpCAZjIQkTnR.; mt=ci=68_1; '
              'enc=WSGJFWg2gtysULUnfqfzLQO7JZ5FhOavCNFH42ikR3oKBm8sVBcSQaL%2F%2FFQwh8nxozuMZwcIkVip2ZYh4zAuMA%3D%3D; '
              'hng=CN%7Czh-CN%7CCNY%7C156; '
              'l=dBMmWRouQcxcgN_0BOfNNYnVz6_TuIOb8sPyyqI_wICP9w1H5n45WZ4KJaYMCnGVHsgyR3oGfmN0BWYpCyCSnxv9-3k_J_mZndC'
              '..; uc1=cookie14=UoTUP2D4E8k1sw%3D%3D&existShop=false&pas=0&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie16'
              '=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU; '
              'isg=BL-_RGfW3YpdFNmWXOHbMcpWTpNJpBNGe3oZClGMGG61YN_iWXSjlj12pjCeOOu- '
}
url = 'https://s.taobao.com/search?q=%E5%9B%BE%E4%B9%A6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id' \
      '=staobaoz_20200326&ie=utf8 '
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        with open('Taobaoresult.txt', 'a', encoding='utf-8') as f:
            f.write(response.text)
            f.close()
    else:
        print('none')
except RequestException:
    print('none')
