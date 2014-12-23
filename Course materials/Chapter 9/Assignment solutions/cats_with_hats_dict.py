theCats = {}

for i in xrange(1, 101):
    theCats[i] = False

for i in xrange(1, 101):
    for cats, hats in theCats.iteritems():
        if cats % i == 0:
            if theCats[cats] is True:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.iteritems():
    if theCats[cats] is True:
        print "Cat {} has a hat.".format(cats)
    else:
        print "Cat {} is hatless!".format(cats)
