import re

string = "My name is Michael Herman"

# re.match(pattern, string, flags=0)
m = re.match(r'(.*) name (.[s]?) .*', string)
# m = re.match(r'(.*) name .[s]? (.*)', string)  # what does this do?

if m:
   print "group(0): ", m.group(0)
   print "group(1): ", m.group(1)
   print "group(2): ", m.group(2)
else:
   print "Sorry. No match!!"