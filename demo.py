import requests as reqs
from bs4 import BeautifulSoup  

r = reqs.get("http://210.70.80.21/~bs109021068/")
r.encoding = "utf8"
if r.status_code == 200:
    #print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    print(soup)
    result1 = soup.find_all("td")
    rint(result1)
else:
    print("no page")