# 14.1 review exercises

import urllib2

# Get the full HTML from the "dionysus" page
myAddress = "http://RealPython.com/practice/dionysus.html"
htmlPage = urllib2.urlopen(myAddress)
htmlText = htmlPage.read()

# Get the "Name" and "Favorite Color" using find()
for tag in ["Name: ", "Favorite Color: "]:
    tagStart = htmlText.find(tag) + len(tag)
    tagEnd = htmlText[tagStart:].find("<")
    # Remove extra spaces and newline padding
    print htmlText[tagStart:tagStart+tagEnd].strip(" \n")


# Get the "Name" and "Favorite Color" using regular expressions
import re
# Match anything up until a new line or HTML tag; non-greedy
for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    matchResults = re.search(tag, htmlText)
    # Remove the "Name: " or "Favorite Color: " label from first result
    result = re.sub(".*: ", "", matchResults.group())
    # Remove extra spaces and newline padding along with opening HTML tag
    print result.strip(" \n<")
