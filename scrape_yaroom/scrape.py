import bs4
import requests as req
import re
# import backoff
import csv
import pandas as pd
import time
import ipaddress
import tqdm


class yaroom(object):

    def __init__(self):
        '''
        law crawler object scrapping question and answer from website hosted by www.66law.cn
        '''
        self.headers = { 
            "Accept":"text/html,application/xhtml+xml,application/xml;9=0.9,*/*;q=0.8",
            "Accept-Encoding":"gzip,deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "X-Forwarded-For": "1.1.1.5",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Host": "dku.yarooms.com",
            "Referer": "http://dku.yarooms.com/",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        self.ip_add = ipaddress.IPv4Network('88.88.88.88')
        self.base_url = r"https://dku.yarooms.com/schedule/weekly?location="
        self.loc_dic ={
            'IB' : 36669,
            'AB' : 16959,
            'CC' : 16960
        }
        self.room_dic = {}

    def cook_soup(self,building):
        '''
        Get beautiful soup object from bs4 and qid or url (To be implemented)
        '''
        url_h = "{}{}".format(self.base_url,self.loc_dic[building])
        url_h = r"https://dku.yarooms.com/account/login?return=https:%2F%2Fdku.yarooms.com%2Fschedule%2Fweekly%3Flocation%3D16959"
        print(url_h)
        html_h = req.get(url_h, timeout=30, headers=self.headers).text
        soup_h = bs4.BeautifulSoup(html_h,'lxml')
        return soup_h

    def scrape_room(self,building):
        '''
        Scrape all rooms in the building that has been passed into.
        '''
        the_soup = self.cook_soup(building)
        # print(the_soup)
        room_dic = {}
        container_div = the_soup.select_one('#content > div.tleft.weekly > div.relative')
        print(container_div)

    
test_scrape = yaroom()
# soup = test_scrape.cook_soup('IB')
# print(soup)
test_scrape.scrape_room('IB')


