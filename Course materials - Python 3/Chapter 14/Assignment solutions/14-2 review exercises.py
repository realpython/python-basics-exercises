# 14.2 review exercises

import urllib2
from bs4 import BeautifulSoup

# Get the full HTML from the "profiles" page
base_URL = "http://RealPython.com/practice/"
address = base_URL + "profiles.html"
html_page = urllib2.urlopen(address)
html_text = html_page.read()
soup = BeautifulSoup(html_text)

# Parse out all the values of the page links
for anchor in soup.find_all("a"):
    # Could also have used urlparse.urljoin() to get absolute URL
    link_address = base_URL + anchor["href"]
    # Display the text in the HTML page of each link
    link_page = urllib2.urlopen(link_address)
    link_text = link_page.read()
    link_soup = BeautifulSoup(link_text)
    print(link_soup.get_text())
