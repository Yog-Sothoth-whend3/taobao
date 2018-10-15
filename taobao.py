from selenium import webdriver
from pyquery import PyQuery as pq
from urllib.parse import urlencode
import time 
import csv,sys,os
import requests
from multiprocessing import Pool ,Process


def start(search_content):
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    bs = webdriver.Chrome(options = opt)
    bs.get('https://www.taobao.com/')

    input_info = bs.find_element_by_id('q')
    time.sleep(2)
    input_info.send_keys(search_content)
    time.sleep(1)

    search_button = bs.find_element_by_class_name('search-button')
    time.sleep(1)
    search_button.click()
    return bs
 
        
def sqlfile():
    with open('iphone.sql','w')as f:
        pass
    
    


def getinfo(content,filename):


    def csvfile(content,filename):
        with open(filename+'.csv','a+',newline='',encoding='utf-8-sig')as f:
            writer = csv.writer(f)
            for i in content:
                price = i('.pic-link.J_ClickStat.J_ItemPicA').attr('trace-price')
                title = i('.J_ItemPic.img').attr('alt')
                lists = [title,price]
                writer.writerow(lists)
    csvfile(content,filename)
    
 
    

    


def nextpage(bs):
    
    nextpage = bs.find_elements_by_css_selector('.J_Ajax.num.icon-tag .icon.icon-btn-next-2')
    for i in nextpage:
        
        i.click()
        time.sleep(2)
        
        return bs      
        
        
        
    

search_key = '葡萄'
bs = start(search_key)
num = 1
while(num):
    doc = pq(bs.page_source)
    content = doc('.item.J_MouserOnverReq').items()
    getinfo(content,search_key)
    bs = nextpage(bs)
    if(num<100):
        num = num + 1
    else:
        break
        

