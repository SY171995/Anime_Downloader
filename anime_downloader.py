from bs4 import BeautifulSoup
import time
import wget
import mechanize
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--anime', dest='a',   help='anime name')
parser.add_argument('--page_of_anime ', dest='page',  help='page of anime')
args=parser.parse_args()
anime=args.a
page=args.page

if anime is None and page is None:
   parser.error("at least one of --foo and --bar required")
   sys.exit()

def site(anime):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    r=br.open('http://animeonline.to/')
    #s=sys.argv[1]
    br.select_form(nr=0)
    br.form['keyword_search'] = anime
    response=br.submit()
    r1=requests.get(str(response.geturl()))
    data = r1.text
    soup = BeautifulSoup(data)
    alink = soup.find_all("a",title=str(anime))
    return alink[0]["href"]





if page is not None:
    r  = requests.get(page,timeout=5)
    data = r.text
    soup = BeautifulSoup(data)

    lepisodes = soup.find_all("div", class_="list_episode")
    a=lepisodes[0].find_all("a")
    for i,d in enumerate(a):
        r1=requests.get(d["href"])
        data = r1.text
        soup = BeautifulSoup(data)
        link=soup.find_all("a", id="download_link")
        r2=requests.get(link[0]["href"])
        data = r2.text
        soup = BeautifulSoup(data)
        alist=soup.find_all("a")
        for j,d1 in enumerate(alist):
            if d1.get_text() == 'Download (360P - mp4':
                wget.download(d1["href"],d.get_text())
        print d.get_text()

else:
    page=site(anime)
    r  = requests.get(page,timeout=5)
    data = r.text
    soup = BeautifulSoup(data)

    lepisodes = soup.find_all("div", class_="list_episode")
    a=lepisodes[0].find_all("a")
    for i,d in enumerate(a):
        r1=requests.get(d["href"])
        data = r1.text
        soup = BeautifulSoup(data)
        link=soup.find_all("a", id="download_link")
        r2=requests.get(link[0]["href"])
        data = r2.text
        soup = BeautifulSoup(data)
        alist=soup.find_all("a")
        for j,d1 in enumerate(alist):
            if d1.get_text() == 'Download (360P - mp4':
                wget.download(d1["href"],d.get_text())
        print d.get_text()



# import urllib2
# from bs4 import BeautifulSoup
#
# fish_url = 'http://animeonline.to/info/hundred'
# page = urllib2.urlopen(fish_url)
# html_doc = page.read()
# soup = BeautifulSoup(html_doc)
#
# print(soup.prettify())


# import mechanize
# import shutil
# import sys
# br = mechanize.Browser()
# br.set_handle_robots(False)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# r=br.open('https://kissanime.to/Anime/Shingeki-no-Kyojin/Episode-004?id=32004')
#
# br.select_form(nr=0)
# br.form['q'] = 'Does mechanize use a real browser?'
# br.submit()
#
# print br.geturl()


#
# from selenium import webdriver
# import sys
# browser = webdriver.Firefox()
# t=browser.get('https://redirector.googlevideo.com/videoplayback?requiressl=yes&id=fee9c336ae2d6412&itag=37&source=webdrive&app=texmex&ip=2a02:5060:502:c049::2&ipbits=32&expire=1465901004&sparams=requiressl%2Cid%2Citag%2Csource%2Cip%2Cipbits%2Cexpire&signature=43820387F52FACBA45E4A13A33CD0302D77223B3.7AF7071796C9D7AA8EDA30673A37434092755B5E&key=ck2&mm=30&mn=sn-2gb7ln7l&ms=nxu&mt=1465886195&mv=u&pl=32?title=(1080P - mp4)Hundred Episode 1')
#
# sys.exit()
#
# all_hover_elements = browser.find_elements_by_class_name("hover-box")


# import mechanize
# import shutil
# import sys
# br = mechanize.Browser()
# br.set_handle_robots(False)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# r=br.open('http://animeonline.to/info/hundred')

#print r.read('https://redirector.googlevideo.com/videoplayback?requiressl=yes&id=fee9c336ae2d6412&itag=37&source=webdrive&app=texmex&ip=2a02:5060:502:c049::2&ipbits=32&expire=1465901004&sparams=requiressl%2Cid%2Citag%2Csource%2Cip%2Cipbits%2Cexpire&signature=43820387F52FACBA45E4A13A33CD0302D77223B3.7AF7071796C9D7AA8EDA30673A37434092755B5E&key=ck2&mm=30&mn=sn-2gb7ln7l&ms=nxu&mt=1465886195&mv=u&pl=32?title=(1080P - mp4)Hundred Episode 1')
#br.select_form(nr=0)
#br.form['q'] = 'Does mechanize use a real browser?'
#br.submit()
