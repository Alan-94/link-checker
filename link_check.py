import requests, bs4

website=input("Wprowadź adres strony: ")
licznik=0
licznik_hrefow=0
res = requests.get(website)
soup = bs4.BeautifulSoup(res.text, "lxml")
links=soup.select('a')
for link in links:
    href=link.get('href')
    if href!= None and href.startswith("http"):
        linkres=requests.get(href)
        licznik_hrefow+=1
        if linkres.status_code==200:
            print(href+"\n link działa")
            licznik+=1
        elif linkres.status_code==999:
            print(href+"\n LINKEDIN - strona nie zezwala na sprawdzanie linków")
        else:
            print(href+"\n NIEDZIAŁAJĄCY LINK. STATUS: "+str(linkres.status_code))
print("Na stronie działa "+str(licznik)+" na "+str(licznik_hrefow)+" linków.")
