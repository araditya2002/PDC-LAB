import pandas as pd
from bs4 import BeautifulSoup
import requests

page=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df=page[0]
company_list=df[df.columns[0]]

for company in company_list:
	url='https://finance.yahoo.com/quote/'+company
	try:
		r=requests.get(url)
		soup = BeautifulSoup(r.text,"html.parser")
		tag=soup.find("meta",attrs={'name':"keywords"})
		meta_data=tag["content"]
		company_name=meta_data.split(",")[1]
		print(company_name)
	except:
		pass

