# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:54:45 2021

@author: amoel.geogy
"""
from selenium import webdriver

PATH = r'C:\Users\amoel.geogy\Documents\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.goodreads.com')
