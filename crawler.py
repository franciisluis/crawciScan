from sqlscan import sqli_scan
import requests
from useragente import useragent
import re
from os import getcwd as pth
class SQLi_Scanner(sqli_scan):
    pass
class teste(object):
    def craw(self, url):
        print(url)
        #padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)
        to_crawl = [url]
        crawled = set()
        cont=0
        while cont < 5:
            header = {'user-agent': useragent()}
            url = to_crawl[0]
            try:
                req = requests.get(url, headers=header, timeout = 12)
            except:
                to_crawl.remove(url)
                crawled.add(url)
                continue

            html = req.text
            links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
            print ('Crawling:', url)
            to_crawl.remove(url)
            crawled.add(url)
            f = open(f'{pth()}/urls.txt', 'a+')
            f.write(f'{url}\n')
            f.close()
            try:
                print(url)
                SQLi_Scanner().scan(url)
            except Exception as e:
                print(e)
            cont = cont + 1
            for link in links:
                if link not in crawled and link not in to_crawl:
                    to_crawl.append(link)
                    #verifica(padrao)