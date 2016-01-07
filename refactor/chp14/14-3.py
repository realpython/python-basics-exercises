# 14.3 review exercises

import mechanicalsoup

my_browser = mechanicalsoup.Browser()
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup

# select the form and fill in the input fields
form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# submit form and show profile page title
profiles_page = my_browser.submit(form, login_page.url)
title = profiles_page.soup.title
print("Title: ", title.text)

# navigate back to login page and show title
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_title = login_page.soup.title
print("Title: ", login_title.text)

# submit form with incorrect values
form = login_html.form
form.select("input")[0]["value"] = "wrong"
form.select("input")[1]["value"] = "password"
error_page = my_browser.submit(form, login_page.url)  # submit form

# check for string
if error_page.soup.text.find("Wrong username or password!") != -1:
    print("Login Failed.")
else:
    print("Login Successful.")
