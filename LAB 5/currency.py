import requests
from lxml import html
import home

base = "https://crypto.com/price/"

def scrape(key, file):
     sym = (key.lower()).replace(' ', '-')
     url = base+sym
     # print(url)
     web = requests.get(url)
     if(web.status_code==200):
          con = html.fromstring(web.text)
          path = '/html/body/div[1]/div[3]/div/div/div[3]/div[1]/div[1]/div[1]/div[1]/h2/span'
          if len(con.xpath(path))>0:
               file.write((key+':\t'+con.xpath(path)[0].text+'\n'))
          else:
               file.write(key+':\t'+"needs manual extraction\n")

     else:
          file.write((key+':\t'+"needs manual extraction\n"))

