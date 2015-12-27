# 14.4 review exercises

from time import sleep
import mechanicalsoup

my_browser = mechanicalsoup.Browser()

# obtain 1 stock quote per minute for the next 3 minutes
for i in range(0, 3):
    
    page = my_browser.get("http://finance.yahoo.com/q?s=yhoo")
    html_text = page.soup
    
    # return a list of all the tags where the id is 'yfs_184_yhoo'
    my_price_tag = html_text.select("#yfs_l84_yhoo")
    # take the BeautifulSoup string out of the first tag
    my_price = my_price_tag[0].text

    # Grab the timestamp
    my_time_tag = page.soup.select("#yfs_market_time")
    my_time = my_time_tag[0].text
    my_time = my_time[:my_time.find(" - ")]  # trim string to just the time

    print("The price of YHOO is: {} on {}".format(my_price, my_time))

    if i<2: # wait a minute if this isn't the last request
        sleep(60)