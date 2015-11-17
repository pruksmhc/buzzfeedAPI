import sys
import requests
import getpass
import pywapi
import lxml.etree as ET
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup 
import urllib



#r = requests.get("http://www.buzzfeed.com/tag/america") 
#r.headers['content-type']
#'text/html'

#r.encoding
#'ISO-8859-1'
#r.apparent_encoding
#'utf-8'
url = "http://www.buzzfeed.com/tag/america"
html = urllib.urlopen(url).read()
print html 
#print soup.get_text()


