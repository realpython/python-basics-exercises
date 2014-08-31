# 14.2 review exercises

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Get the full HTML from the "profiles" page
base_URL = "https://realpython.com/practice/"
address = base_URL + "profiles.html"
html_page = urlopen(address)
html_text = html_page.read().decode('utf-8')
soup = BeautifulSoup(html_text)

# Parse out all the values of the page links
for anchor in soup.find_all("a"):
    # Could also have used urlparse.urljoin() to get absolute URL
    link_address = base_URL + anchor["href"]
    # Display the text in the HTML page of each link
    link_page = urlopen(link_address)
    link_text = link_page.read().decode('utf-8')
    link_soup = BeautifulSoup(link_text)
    print(link_soup.get_text())
