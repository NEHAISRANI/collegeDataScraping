#BeautifulSoup is a python library for pulling data from htl and  xml files 
from bs4 import BeautifulSoup
# pprint used for makes our code beautiful. 
from pprint import pprint
import urllib3


list1=[] 
http = urllib3.PoolManager() #using PoolManager library for receiving the data from  http 
r = http.request('GET', 'https://www.collegedekho.com/colleges-in-pune/')
soup=BeautifulSoup(r.data,"html.parser")
row = soup.find("div",class_="container collegeListingContent")
row_s = row.find_all("div",class_="listing-content rightside")
for i in row_s:
    Title=i.find_all("div",class_="col-md-12")
    for j in Title:
        collegeInfo=j.find("div",class_="collegeinfo")
        data=collegeInfo.find("div","title").a.get_text()
        print(data)
button=i.find("div",class_="loadmorebtn").get_text()
print(button)       

        
