# Modify the variable value so that all of the `print` statements return `True`.

import re

zero = "Python"
one = "5/25/2014"
two = "A88 8AA"
three = '\w\d\w\s\w\d\w'
four = "$4.76"
five = ["haaaappy", "birthday"]
six = r'\.(doc|odt)$'
seven = "My email is (email redacted)"

# zero = "Ruby"
# one = "5/25/14"
# two = "A99 9AA"
# three = r''
# four = "6.76"
# five = ["happy","birthday"]
# six = r'\.(doc)$'
# seven = "My email is michael@mherman.org"

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# -------------------------------------- #

print "zero:  {}".format(
    zero == re.search(r'[P].*', "This is Real Python").group())
print "one:   {}".format(
    one == re.search(r'\d{1,2}\/\d{1,2}\/\d{4}', "5/25/2014").group())
print "two:   {}".format(
    two == re.match(
        r'[A-Z]([A-Z](\d{1,2}|\d[A-Z])|\d{1,2})\s\d[A-Z]{2}',
        "A88 8AA",
        re.VERBOSE
    ).group()
)
print "three: {}".format(bool(re.search(three, "B4c r79").group()))
print "four:  {}".format(bool(re.search(r'\$[0-5]\.\d\d', four)))
print "five:  {}".format(bool(re.search(r'\ha{4,10}ppy\b', five[0])))
files = ['test.doc', 'test.odt', 'test.ddt', 'doc', 'testodt', 'test.doc']
matched_files = [file for file in files if re.search(six, file)]
print "six:   {}".format(len(matched_files) == 3)
email_regex = r'\w+@\w+\.(com|org|edu|net)'
text = "My email is michael@mherman.org"
redacted_text = re.sub(email_regex, '(email redacted)', text)
print "seven: {}".format(seven == redacted_text)
