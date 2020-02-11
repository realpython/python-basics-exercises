# 16.1 - Scrape and Parse Text From Websites
# Solutions to review exercises

from urllib.request import urlopen

# Exercise 1
# Get the full HTML from the "dionysus" page
url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

# Exercise 2
# Get the "Name" and "Favorite Color" using .find()
for tag in ["Name: ", "Favorite Color: "]:
    tag_start = html_text.find(tag) + len(tag)
    tag_end = html_text[tag_start:].find("<")
    # Remove extra spaces and newline padding
    print(html_text[tag_start : tag_start + tag_end].strip(" \n"))


# Exercise 3
# Get the "Name" and "Favorite Color" using regular expressions
import re

# Match anything up until a new line or HTML tag; non-greedy
for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)
    # Remove the "Name: " or "Favorite Color: " label from first result
    result = re.sub(".*: ", "", match_results.group())
    # Remove extra spaces and newline padding along with opening HTML tag
    print(result.strip(" \n<"))
