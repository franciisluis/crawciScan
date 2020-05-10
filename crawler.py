from sqlscan import sqli_scan
import requests
from useragente import useragent
import re
class SQLi_Scanner(sqli_scan):
    pass
class teste(object):
    def craw(url):
        padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)
        to_crawl = [url]
        crawled = set()
        cont=0
        while cont<10:
            url = to_crawl[0]
            header = {'user-agent': useragent()}
            try:
                req = requests.get(url, headers=header)
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
            SQLi_Scanner().scan(url)
            cont=cont + 1
            for link in links:
                if link not in crawled and link not in to_crawl:
                    to_crawl.append(link)
                    #verifica(padrao)
    def verifica(padrao):
        print(padrao)
        injecao = padrao.groups()[0] + '\''
        print(injecao)
        header = {'user-agent': useragent()}
        req = requests.get(injecao, headers=header)

        html = req.text

        if 'mysql_fetch_array()' in html:
            print('Vulneravel')
        else:
            print('Não vulneravel')