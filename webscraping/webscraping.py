import time

from bs4 import BeautifulSoup as bs4
import requests

# ------上級編------------
class Scp(object):

    __version__ = '3.0.1'

    def set_url_and_tag(self, url, tag, attrs={}):
        
        if 'https://' not in url:
            raise ValueError(
                    'Invalid URL:Example is https://example.com/.')
        
        time.sleep(1)
        request = requests.get(url)
        soup = bs4(request.content, 'html.parser')
        value = soup.find_all(tag, attrs=attrs)
        datas = []

        for val in value:
            datas.append(val.text)
        return datas

# ------上級編デバッグ用--------
# if __name__ == '__main__':
#     scp = Scp()
#     url = 'https://zerofromlight.com/blogs/'
#     tag = 'h5'
#     attrs = {}
#  
#     datas = scp.set_url_and_tag(url, tag, attrs=attrs)
#     print(datas)


# ------中級編------------
# def set_url_and_tag(url, tag, attrs={}):
#     
#     if 'https://' not in url:
#         raise ValueError(
#                 'Invalid URL:Example is https://example.com/.')
#     
#     time.sleep(1)
#     request = requests.get(url)
#     soup = bs4(request.content, 'html.parser')
#     value = soup.find_all(tag, attrs=attrs)
#     datas = []
# 
#     for val in value:
#         datas.append(val.text)
#     return datas
# 
# # ------中級編デバッグ用--------
# if __name__ == '__main__':
#     url = 'zerofromlight.com/blogs/'
#     tag = 'h5'
#     attrs = {}
#     datas = set_url_and_tag(url, tag, attrs=attrs)
#     print(datas)


# ------初級編２------------
# def set_url_and_tag(url, tag, attrs={}):
#     
#     time.sleep(1)
#     request = requests.get(url)
#     soup = bs4(request.content, 'html.parser')
#     value = soup.find_all(tag, attrs=attrs)
#     datas = []
# 
#     for val in value:
#         datas.append(val.text)
#     datas = tuple(datas)
#     return datas
# 
# # ------初級編２デバッグ用--------
# if __name__ == '__main__':
#     url = 'https://zerofromlight.com/blogs/'
#     tag = 'h5'
#     attrs = {}
#     datas = set_url_and_tag(url, tag, attrs=attrs)
#     print(datas)


# ------初級編------------
# url = 'https://zerofromlight.com/blogs/'
# tag = 'h5'
# request = requests.get(url)
# soup = bs4(request.content, 'html.parser')
# value = soup.find_all(tag)
# datas = []
# 
# for val in value:
#     datas.append(val.text)
# 
# print(datas)

