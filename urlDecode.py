#!/usr/bin/env python
#Simple script to un-shorten the shortened URLs using the website - URLXray.com
# Author: Rahul Binjve (@RahulBinjve)
# Usage: ./urlDecode.py URL

import urllib2
from bs4 import BeautifulSoup
import sys

def main():
    if len(sys.argv) < 2:
        print "\nUsage: urlDecoder.py \"URL You Want to decode\""
        sys.exit(1)
       
    result = decode(sys.argv[1])
    print "\nDecoded URL is -> ", result

#Decode function, all our work will be done here.
def decode(userArg):
     
    url = "http://urlxray.com/display.php?url=" + userArg
    print "\nUser provided URL -> ", userArg
       
    webPage = urllib2.urlopen(url)
    tastySoup = BeautifulSoup(webPage)
    div = str(tastySoup.find_all("div", class_ = "resultURL2"))
    tastySoup = BeautifulSoup(div)
    for a in tastySoup.findAll('a'):
        if a.has_key('href'):
            decoded = a['href']
    if decoded:
        return decoded

#Standard Python Boilerplate
if __name__ == '__main__':
        main()

