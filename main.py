import time
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
rest_name=[]
rest_image=[]
rest_category=[]
rest_description=[]
rest_location=[]
item_names=[]
item_prices=[]
item_images=[]
item_category=[]

images=[]
# url="https://www.allmenus.com/ga/atlanta/-/"
url="https://www.allmenus.com/ga/atlanta/-/"
# url=input("Enter url of shop :- ")
options = webdriver.ChromeOptions() #newly added 
# options.headless = True #newly added 
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 
driver.get(url)

# ------------------------------   WORKING  -----------------------------
item_cat=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[1]/section[1]/div[2]/div[2]/div/label/a')
all=[]
for i in item_cat:
    all.append(i.get_attribute("href"))
all_rest=[]
f=open("all_rests_link.txt","a")
for i in all:
    driver.get(i)
    rests_all=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/section[2]/div[2]/ul/li/div/div[1]/h4/a')
    for r in rests_all:
        all_rest.append(r.get_attribute("href"))
        print(r.get_attribute("href"))
        f.write(f'{r.get_attribute("href")}\n')   
##############################

#------------All REST URL DONE-----------------------

#################################






























