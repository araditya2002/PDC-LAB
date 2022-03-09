import pandas as pd
from bs4 import BeautifulSoup
import requests
import queue
import time
from threading import Thread

def crawler(company):
	print(company)
	url='https://finance.yahoo.com/quote/'+company
	r=requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")	
	tag=soup.find("meta",attrs={'name':"keywords"})["content"].split(",")[1]
	meta_data=tag["content"]
	company_name=meta_data.split(",")[1]
	return company_name
	
page=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df=page[0]
company_list=df[df.columns[0]]
company_name=[]
threads=[]
que=queue.Queue()
for company in company_list:
	t = Thread(target=lambda q, arg1: q.put(crawler(arg1)), args=(que, company))
	t.start()
	threads.append(t)
for t in threads:
	t.join()
while len(company_name)!=len(company_list):
	company_name.append(que.get())
	
print(company_name)
	
	