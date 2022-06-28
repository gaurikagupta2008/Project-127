from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.m.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(r"C:\Users\gauri\OneDrive\Desktop\Python\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
page=requests.get(browser)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")
temp_list=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
star_name=[]
star_distance=[]
star_mass=[]
star_radius=[]
for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][5])
    star_radius.append(temp_list[i][6])
df2=pd.dataframe(list(zip(star_name,star_distance,star_mass,star_radius)),column=["star_name","star_disctance","star_mass","star_radius"])
df2.to_csv("scrap_project_1")

    