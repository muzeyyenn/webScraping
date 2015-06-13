
# coding: utf-8

import requests
from bs4 import BeautifulSoup

url="http://tr.softonic.com/t/pc-oyunlar%C4%B1"
r1=requests.get(url)
mainpage=BeautifulSoup(r1.content)

types=mainpage.find("div",id="content_2col_right_list").find("ul").findAll("li")

links=[]
for i in types:
    link=i.find("a").get("href")
    links.append(link)
    
data={'name':'','type':'','puan':'','rateCount':'','status':''}
obj=[]

for i in links:
    typepage=requests.get(i)
    itempage=BeautifulSoup(typepage.content)
    
  
    games=itempage.find("table",id="program_list").findAll("tr")
    for i in games:
        types= itempage.title.text
        name= i.find("div",class_="basic_info").find("h5").find("strong").text
        rate= i.find("td",class_="rating_description").find("span",class_="middle_value").text
        count= i.find("td",class_="downloads_description").find("dd").text
        status= i.find("div",class_="basic_info").find("dd",class_="license2").text
        data={'name':name,'types':types,'puan':rate,'rateCount':count,'status':status}
        obj.append(data)
    try:    
        nextpage=itempage.find("ul",class_="nav_pagination").findAll("a")

        for i in nextpage:
            link_next=i.get("href")
            rnext=requests.get("http://tr.softonic.com/"+link_next)
            next_page=BeautifulSoup(rnext.content)
            games_next=next_page.find("table",id="program_list").findAll("tr")
            for i in games_next:
                types= next_page.title.text
                name= i.find("div",class_="basic_info").find("h5").find("strong").text
                rate= i.find("td",class_="rating_description").find("span",class_="middle_value").text
                count= i.find("td",class_="downloads_description").find("dd").text
                status= i.find("div",class_="basic_info").find("dd",class_="license2").text
                data={'name':name,'types':types,'puan':rate,'rateCount':count,'status':status}
                obj.append(data)

    except:
        pass

with open('games.json', 'w') as outfile:
    json.dump(obj, outfile)

