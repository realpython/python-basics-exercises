# 8.6.2 coin_toss_alternative.py
# Simulate the results of a series of coin tosses and track the results

from __future__ import division
from random import randint


trials = 100000
flips = 0

for trial in range(1, trials):
    first_flip = randint(0, 1)
    flips += 1
    while randint(0, 1) == first_flip:
        flips += 1
    flips += 1

print "The average number of coin flips was {0}".format(flips/trials)
