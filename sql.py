import sys,argparse
import requests
import re
from useragente import useragent
from os import getcwd as pth
from sqlscan import sqli_scan
from dork import Parser
from cor import logo
from cor import color as c
urls=[]
class crawl(object):
    auth = {
        1: [
            'https://www.google.com',
            'class="r"><a href="/url\?q=(.*?)&amp',
            'fl'
        ],
        2: [
            'https://www.bing.com',
            'h=".*?" href="(h.*?")',
            "b_widePag sb_bp"
        ],
        3:[
            'https://search.yahoo.com/',
            '<a href="/url\?q=(.*?)'
        ]
    }
    def __init__(
            self,
            dork,
            proxy=None
    ):
        self.dork = dork
        self.proxy = proxy

    def Bing(self):
        bing = Parser(
            self.dork,
            crawl.auth[2][0],
            crawl.auth[2][1],
            crawl.auth[2][2],
            proxy=self.proxy
        )
        bing.request()
        for url in dir(bing):
            if 'go.microsoft.com' in url or 'bing.com' in url:
                pass
            else:
                urls.append(url)
    def Google(self):
        google = Parser(
            self.dork,
            crawl.auth[1][0],
            crawl.auth[1][1],
            crawl.auth[1][2],
            proxy = self.proxy
        )
        google.request()
        for url in dir(google):
            if 'go.microsoft.com' in url or 'bing.com' in url:
                pass
            else:
                urls.append(url)
    def Yahoo(self):
        yahoo = Parser(
            self.dork,
            crawl.auth[3][0],
            crawl.auth[3][2],
            crawl.auth[3][3],
            proxy = self.proxy
        )
        yahoo.request()
        for url in dir(yahoo):
            if 'go.microsoft'in url or 'bing.com' in url:
                pass
            else:
                urls.append(url)
class SQLi_Scanner(sqli_scan):
    pass


class Main():
    if sys.version[0] in '2':
        print("\n Não suportado por python 2.x. Utilize python 3.0 \n")
        exit()
    fel = sys.argv[0]
    par = argparse.ArgumentParser(
        prog=fel,
        usage="%(prog)s --dork [keyword]  --scan",
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
    Description:
    - Codename: CrawciScan 
    + Crawler utilizando Google Dork + Bing Dork + Yahoo Dork
    + Scanner vulnerabilidade de SQLI
    BY: Francis Luis
    """)
    par.add_argument(
        '--dork',
        help="""
        Digite a url inurl:.php?id=""",
        metavar='[keywords]',
        type=str
    )
    par.add_argument(
        '--proxy',
        help="""
        Para usar o proxy siga o exemplo 127.0.0.1:8085
        com autenticacao user@password:127.0.0.1:8085""",
        metavar='[proxy:port]',
        type=str,
        action='store',
        default=None
    )
    par.add_argument(
        '--scan',
        help="""
        Para fazer o Scanner de vulnerabilidades SQLI utilize o arumento --scan""",
        action="store_true"
    )
    arg=par.parse_args()
    print(arg)
    try:
        if arg.scan:
            if arg.dork != None:
                print(logo())
                _ = crawl(arg.dork,proxy=arg.proxy)
                _.Bing()
                _.Google()
                if urls != []:
                    for url in list(set(urls)):
                        print('- {}'.format(url))
                    for scan in list(set(urls)):
                        try:
                            SQLi_Scanner().scan(scan)
                        except Exception as e:
                            print(e)
                else:
                    print('\n{}[-]{} URL não encontrada!\n'.format(c.R,c.W))
            else:
                par.print_help()
        elif not arg.scan:
            if arg.dork != None:
                print(logo())
                _ = crawl(arg.dork, proxy=arg.proxy)
                _.Bing()
                _.Google()
                if urls != []:
                    for url in list(set(urls)):
                        print('- {}'.format(url))
                else:
                    print('\n{}[-]{} URL não encontrada!\n'.format(c.R,c.W))
            else:
                par.print_help()
        else:
            par.print_help()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        exit()

class Main():
    pass