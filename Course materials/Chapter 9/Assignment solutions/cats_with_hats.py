def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    for num in xrange(1, 100+1):
        for cat in xrange(1, 100):
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
    for cat in xrange(1, 100):
        if cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on

cats = [False] * 100
print get_cats_with_hats(cats)
