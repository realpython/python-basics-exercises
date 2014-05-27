def total_enrollment(list_of_universities):

    # variables
    total_students = 0
    total_tuition = 0

    # iterate through lists, adding values
    for university in universities:
        total_students += university[1]
        total_tuition += university[2] * university[1]

    # return variables
    return total_students, total_tuition


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# call function
print(total_enrollment(universities))