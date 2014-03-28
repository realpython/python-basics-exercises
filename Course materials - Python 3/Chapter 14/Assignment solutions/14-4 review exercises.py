# 14.4 review exercises

from time import sleep
import mechanize
from bs4 import BeautifulSoup

# Create a Browser object
myBrowser = mechanize.Browser()

# Obtain 1 stock quote per minute for the next 3 minutes
for i in range(0, 3):
    htmlPage = myBrowser.open("http://finance.yahoo.com/q?s=yhoo")
    htmlText = htmlPage.get_data()

    mySoup = BeautifulSoup(htmlText)

    # Grab the BeauitfulSoup stock quote string
    myPriceTags = mySoup.find_all("span", id="yfs_l84_yhoo")
    myPrice = myPriceTags[0].string

    # Grab the timestamp
    myTimeTags = mySoup.find_all("span", id="yfs_market_time")
    myTime = myTimeTags[0].string
    myTime = myTime[:myTime.find(" - ")] # trim string to just the time
    
    print "The price of YHOO is: {} on {}".format(myPrice, myTime)

    if i<2: # Wait a minute if this isn't the last request
        sleep(60)

