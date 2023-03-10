
import csv
import json
import requests
from bs4 import BeautifulSoup


# print(type(data))
REST_URL=[]
REST_NAME=[]
REST_CATEGORY=[]
REST_PHONE=[]
REST_ADDRESS=[]
ITEM_NAME=[]
ITEM_PRICE=[]
ITEM_CATEGORY=[]
# opening the file

def main(url,writer):
    # making request
    # url = 'https://www.allmenus.com/ga/atlanta/137033-seattles-best-coffee/menu/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_items = soup.find_all('script')[0]
    json_string = menu_items.string
    data = json.loads(json_string)
    print("")
    print("")
    print("")
    print("")
    print(type(data))

    # getting the rest data 

    rest_name=soup.find('div',class_="s-col-lg-8 s-col-xs-12 restaurant-summary").find("h1").text
    rest_phone=soup.find('div',class_="s-col-lg-8 s-col-xs-12 restaurant-summary").find("div",class_="phone").text.replace("\n","")
    rest_address=soup.find('a',class_="menu-address").text

    # getting menu data
    
    rest_cat=data['servesCuisine'][0]
    for i in data['hasMenu']:
        timing=i['name']
        for c in i['hasMenuSection']:
            category=c['name']
            for p in c['hasMenuItem']:
                print(p)
                try:
                    name=p['name']
                except:
                    name=""
                try:
                    price=p['offers'][0]['Price']
                    priceCurrency=p['offers'][0]['priceCurrency']
                except:
                    price=''
                    priceCurrency=''
                data=[url,rest_name,rest_cat,rest_phone,rest_address,timing,category,name,price,priceCurrency]
                writer.writerow(data)

f= open('data.csv', mode='a', newline='') 
writer = csv.writer(f)
data=["REST_URL","REST_NAME","REST_CATEGORY","REST_PHONE","REST_ADDRESS","ITEM_TIMING","ITEM_CATEGORY","ITEM_NAME","ITEM_PRICE","ITEM_CATEGORY"]
writer.writerow(data)
with open('all_rests_link.txt') as f:
    lines = f.readlines()
    for i in lines:
        try:
            main(i,writer)
        except:
            pass



   




