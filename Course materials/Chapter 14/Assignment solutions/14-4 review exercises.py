# 14.4 review exercises

from time import sleep
import mechanize
from bs4 import BeautifulSoup

# Create a Browser object
my_browser = mechanize.Browser()

# Obtain 1 stock quote per minute for the next 3 minutes
for i in range(0, 3):
    html_page = my_browser.open("http://finance.yahoo.com/q?s=yhoo")
    html_text = html_page.get_data()

    my_soup = BeautifulSoup(html_text)

    # Grab the BeauitfulSoup stock quote string
    my_price_tags = my_soup.find_all("span", id="yfs_l84_yhoo")
    my_price = my_price_tags[0].string

    # Grab the timestamp
    my_time_tags = my_soup.find_all("span", id="yfs_market_time")
    my_time = my_time_tags[0].string
    my_time = my_time[:my_time.find(" - ")]  # trim string to just the time

    print "The price of YHOO is: {} on {}".format(my_price, my_time)

    if i < 2:  # Wait a minute if this isn't the last request
        sleep(60)
