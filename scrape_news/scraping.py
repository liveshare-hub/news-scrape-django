import requests
from bs4 import BeautifulSoup
import json

def get_news(url):
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    judul = soup.h1.text
    teaser = soup.p.text
    berita = soup.find_all('div',{'class':'sc-bBrHrO sc-cxabCf bTxTGD jNSwiR sc-gspIFj dcJlbT rich-text has-italic'})
    img_url = 'https://www.bing.com/images/search?q='+judul.replace(' ','+')
    data_img = requests.get(img_url)
    
    img_soup = BeautifulSoup(data_img.text, 'html.parser')
    div = img_soup.find_all('div',{'class':'infopt'})
   
    links = 'https://www.bing.com'+div[0].find('a')['href']
    d_url = requests.get(links)
    d = BeautifulSoup(d_url.text, "html.parser")
    e = d.find_all('div')
    print(d)
        
        # print(i.find('li').find('a')['href'])
    # print(div[0].find('li').find('a')['href'])
    
    # img = soup.find_all('img',{'class':'hq-img loaded'})
    
    for div in berita:
        val = [p.text for p in div.find_all('p')]
    # data = [judul, teaser, val]
    # print(img)
    data = {
        'judul':judul,
        'teaser':teaser,
        'berita':val
    }
    # print(json.dumps(data))
    return data