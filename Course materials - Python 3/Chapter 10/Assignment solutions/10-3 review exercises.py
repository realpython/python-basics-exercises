# 10.3 review exercises

import mechanize
from bs4 import BeautifulSoup

# Start a mechanize browser and open the login page
myBrowser = mechanize.Browser()
myBrowser.open("http://RealPython.com/practice/login.php")

# Select the login form and input a username & password
myBrowser.select_form("login")
myBrowser["user"] = "zeus"
myBrowser["pwd"] = "ThunderDude"
myResponse = myBrowser.submit() # submit form

# Make sure we were redirected to the profiles page
print myResponse.geturl()

# Return to the previous login page
myBrowser.back()

# Try to log in with incorrect information
myBrowser.select_form("login")
myBrowser["user"] = "Hera"
myBrowser["pwd"] = "LightningLady"
myResponse = myBrowser.submit() # submit form

# See if we were redirected to the "error" page by searching for known text
if myResponse.get_data().find("Wrong username or password!") != -1:
    print "Login failed."
else:
    print "Login success."

