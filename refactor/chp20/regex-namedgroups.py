import re

string = "Michael Herman"

# re.match(pattern, string, flags=0)
m = re.match(r"(?P<first>\w+)\W+(?P<last>\w+)", string)

if m:
    print("group(0) : ", m.group(0))
    print("group(1) : ", m.group(1))
    print("group(2) : ", m.group(2))
    print("")
    print('group("first") : ', m.group("first"))
    print('group("last") : ', m.group("last"))
else:
    print("Sorry. No match!!")
