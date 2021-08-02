# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:54:45 2021

@author: amoel.geogy
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

PATH = r'C:\Users\amoel.geogy\Documents\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.goodreads.com/book')

books = ['harry potter and the chamber of secrets']
bookid = []

search = driver.find_element_by_id('explore_search_query')
search.send_keys(books[0])
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a'))
    )
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a').click()
    print('clicked')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]'))
    )
    time.sleep(1)
    # print(driver.current_url)
    ab = driver.current_url
    bookid.append(driver.current_url.split('/')[-1].split('?')[0])
    print(bookid[0])
    print('bookid received')
except:
    print('something went wrong')
    pass

import requests

url = 'https://www.goodreads.com/book/show/' + bookid[0]
url
res = requests.get(url).text

with open("res.txt", "w", encoding='utf-8') as text_file:
    text_file.write(res)

soup = BeautifulSoup(res,features='html')
soup.prettify()

import sys
sys.executable
import wordcloud