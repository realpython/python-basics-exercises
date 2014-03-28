# 10.2 review exercises

import urllib2
from bs4 import BeautifulSoup

# Get the full HTML from the "profiles" page
baseURL = "http://RealPython.com/practice/"
address = baseURL + "profiles.html"
htmlPage = urllib2.urlopen(address)
htmlText = htmlPage.read()
soup = BeautifulSoup(htmlText)

# Parse out all the values of the page links
for anchor in soup.find_all("a"):
    # Could also have used urlparse.urljoin() to get absolute URL
    linkAddress = baseURL + anchor["href"]
    # Display the text in the HTML page of each link
    linkPage = urllib2.urlopen(linkAddress)
    linkText = linkPage.read()
    linkSoup = BeautifulSoup(linkText)
    print linkSoup.get_text()

