import re
from phone_list import data


def parse_phone_book(phone_book):
    for line in phone_book:
        if re.search(r'K.*Hardy', line['name']):
            print "{} - {}".format(line['name'], line["phone"])

parse_phone_book(data)
