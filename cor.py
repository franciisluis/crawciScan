# -*- coding: utf-8 -*-
import sys
from time import sleep, localtime


class color(object):
    if sys.platform in ['linux', 'linux2']:
        R = '\033[91m'
        G = '\033[92m'
        B = '\033[94m'
        Y = '\033[93m'
        W = '\033[0m'
    else:
        R = ''
        G = ''
        B = ''
        Y = ''
        W = ''


class logo(color):

    def __init__(self):
        pass

    def __str__(self):
        _ = color
        return f'''
{_.G}                                        _ ____                  
{_.G}      ___ _ __ __ ___      ___ __   ___(_) ___|  ___ __ _ _ __  
{_.G}     / __| '__/ _` \ \ /\ / / '_ \ / __| \___ \ / __/ _` | '_ \ 
{_.G}    | (__| | | (_| |\ V  V /| | | | (__| |___) | (_| (_| | | | |        
{_.G}     \___|_|  \__,_| \_/\_/ |_| |_|\___|_|____/ \___\__,_|_| |_|                                      

{_.Y} Codename{_.W} : {_.B}CrawnciScan{_.W}
{_.R} By{_.W} : {_.G}Francis Luis{_.W}

          '''


def load():
    _ = localtime()
    x = [
        '|', '\\', '-', '/'
    ]
    for y in x:
        print(f'\r [{y}]',
              end=' Starting At %s %s-%s-%s%s - %s:%s  ' % (color.G, _[0], _[1], _[2], color.W, _[3], _[4]))
        sys.stdout.flush()
        sleep(0.15)




