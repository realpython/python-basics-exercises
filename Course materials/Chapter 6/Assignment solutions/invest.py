# 6.3 invest.py
# calculate compound interest to track the growth of an investment


def invest(amount, rate, time):
    print "principal amount: ${}".format(amount)
    print "annual rate of return:", rate
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print "year {}: ${}".format(t, amount)
    print

invest(100, .05, 8)
invest(2000, .025, 5)
