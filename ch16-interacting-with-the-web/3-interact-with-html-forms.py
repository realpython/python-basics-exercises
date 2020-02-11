# 16.3 - Interact with HTML Forms
# Solutions to review exercises

# Make sure BeautifulSoup is installed first with:
# pip3 install MechanicalSoup

import mechanicalsoup


# Exercise 1
browser = mechanicalsoup.Browser()
login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup

# select the form and fill in the input fields
form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# submit form
profiles_page = browser.submit(form, login_page.url)


# Exercise 2
# show profile page title
title = profiles_page.soup.title
print(f"Title: {title.text}")


# Exercise 3
# navigate back to login page and show title
login_page = browser.get(login_url)
login_title = login_page.soup.title
print(f"Title: {login_title.text}")


# Exercise 4
# Submit form with incorrect values
form = login_html.form
form.select("input")[0]["value"] = "wrong"
form.select("input")[1]["value"] = "password"
error_page = browser.submit(form, login_page.url)

# check for string
if error_page.soup.text.find("Wrong username or password!") != -1:
    print("Login Failed.")
else:
    print("Login Successful.")
