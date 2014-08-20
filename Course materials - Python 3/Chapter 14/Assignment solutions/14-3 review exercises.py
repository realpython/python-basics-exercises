# 14.3 review exercises

import mechanize
# from bs4 import BeautifulSoup

# Start a mechanize browser and open the login page
my_browser = mechanize.Browser()
my_browser.open("http://RealPython.com/practice/login.php")

# Select the login form and input a username & password
my_browser.select_form("login")
my_browser["user"] = "zeus"
my_browser["pwd"] = "ThunderDude"
my_response = my_browser.submit()  # submit form

# Make sure we were redirected to the profiles page
print(my_response.geturl())

# Return to the previous login page
my_browser.back()

# Try to log in with incorrect information
my_browser.select_form("login")
my_browser["user"] = "Hera"
my_browser["pwd"] = "LightningLady"
my_response = my_browser.submit()  # submit form

# See if we were redirected to the "error" page by searching for known text
if my_response.get_data().find("Wrong username or password!") != -1:
    print("Login failed.")
else:
    print("Login success.")
