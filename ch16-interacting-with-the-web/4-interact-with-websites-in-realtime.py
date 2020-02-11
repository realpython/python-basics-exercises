# 16.4 - Interact With Websites in Real-Time
# Solutions to review exercise

# Make sure BeautifulSoup is installed first with:
# pip3 install MechanicalSoup

from time import sleep
import mechanicalsoup

my_browser = mechanicalsoup.Browser()

# Obtain 1 dice roll result every 10 seconds for the next minute
for i in range(0, 6):
    page = my_browser.get("http://olympus.realpython.org/dice")
    html_text = page.soup

    # Return a list of all the tags where the id is 'yfs_184_yhoo'
    dice_result_tag = html_text.select("#result")

    # Take the BeautifulSoup string out of the first tag
    dice_result = dice_result_tag[0].text

    # Grab the timestamp
    time_tag = page.soup.select("#time")
    time = time_tag[0].text
    time = time[: time.find(" - ")]  # Trim string to just the time

    print(f"Rolled a '{dice_result}' on {time}")

    if i < 5:  # Wait 10 seconds if this wasn't the last request
        sleep(10)
