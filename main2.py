#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 15:28:46
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os
import re
import json
import time
import requests
from time import sleep
from utils import RedisDB
from crawl import get_city,Xchtl,get_prices,dl_cmt_page

db = RedisDB()


def main():
    while db.get_data_count('xchtl:hotels')>0:
        hotel = db.get_data('xchtl:hotels')
        print(hotel)
        try:
            hotel['price'] = get_prices(hotel['url'])
            dl_cmt_page(hotel)
        except Exception as e:
            print(e)
            db.write_data('xchtl:hotels',hotel)
        finally:
            val = os.system("ps aux|grep chrome|awk '{print $2}'|xargs kill -9")
            print(val,'--------------------------------')
            val2 = os.system("rm -rf /tmp/.com.google.Chrome.*")
            print(val2, '--------------------------------')
            time.sleep(5)




if __name__ == '__main__':
    main()
