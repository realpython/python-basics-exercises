# 1.14.2 - Use an HTML Parser to Scrape Websites
# Solutions to review exercises

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Exercise 1
# Get the full HTML from the "profiles" page
base_URL = "http://olympus.realpython.org"
address = base_URL + "/profiles"
html_page = urlopen(address)
html_text = html_page.read().decode('utf-8')
soup = BeautifulSoup(html_text)

# Exercise 2
# Parse out all the values of the page links
for anchor in soup.find_all("a"):
    # Could also have used urlparse.urljoin() to get absolute URL
    link_address = base_URL + anchor["href"]

    # Exercise 3
    # Display the text in the HTML page of each link
    link_page = urlopen(link_address)
    link_text = link_page.read().decode('utf-8')
    link_soup = BeautifulSoup(link_text)
    print(link_soup.get_text())
