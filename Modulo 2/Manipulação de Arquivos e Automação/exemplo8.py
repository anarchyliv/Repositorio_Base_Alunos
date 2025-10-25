from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.globo.com/")
soup = BeautifulSoup(res.text,"html.parser")
print(soup.title)
print(soup.title.string)
link= soup.select("a") # Selecione todas as tags a 
for link in link[:5]:
    print(link.get("href"))