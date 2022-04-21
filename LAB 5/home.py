import bs4, requests
from lxml import html

url = "https://crypto.com/price"

# writes the names of the currencies to this file
# will be used in the value scraping phase
wfile = 'inter.txt'

def scrape():
     file = open(wfile, 'w')
     print("scraping currency names")
     web = requests.get(url)
     con = html.fromstring(web.text)
     for i in range(1,51):
          path = f"/html/body/div[1]/div[3]/div[2]/div/div[4]/div[1]/table/tbody/tr[{i}]/td[3]/div/div[2]/span[1]"
          file.write(((con.xpath(path)[0].text)+'\n'))

# scrape()