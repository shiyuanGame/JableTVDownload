import argparse
from bs4 import BeautifulSoup
import random
from urllib.request import urlretrieve
from urllib.request import Request, urlopen
from config import headers
import re


def get_parser():
    parser = argparse.ArgumentParser(description="Jable TV Downloader")
    parser.add_argument("--random", type=bool, default=False,
                        help="Enter True for download random ")
    parser.add_argument("--url", type=str, default="",
                        help="Jable TV URL to download")
    parser.add_argument("--all-urls", type=str, default="",
                        help="Jable URL contains multiple avs")

    return parser


def av_recommand():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://jable.tv/'
    request = Request(url, headers=headers)
    web_content = urlopen(request).read()
    # 得到繞過轉址後的 html
    soup = BeautifulSoup(web_content, 'html.parser')
    h6_tags = soup.find_all('h6', class_='title')
    av_list = re.findall(r'https[^"]+', str(h6_tags))
    return random.choice(av_list)


def changeName(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    # url = url
    request = Request(url, headers=headers)
    # request.timeout = 10000
    print(request)
    web_content = urlopen(request).read()
    print(web_content)

    # 得到繞過轉址後的 html
    soup = BeautifulSoup(web_content, 'html.parser')
    print(soup)
    h1 = soup.find('title')
    name = str(h1)[7:-41:1]
    print("name:" + name)
    # name = h1[7:-20:1]
    return name
# print(av_recommand())
