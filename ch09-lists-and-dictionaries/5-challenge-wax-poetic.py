# 9.5 - Challenge: Wax Poetic
# Solution to challenge


# Generate a random poem based on a set structure

from random import choice

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


def make_poem():
    """Create a randomly generated poem, returned as a multi-line string."""
    # Pull three nouns randomly
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)
    # Make sure that all the nouns are different
    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

    # Pull three different verbs
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)

    # Pull three different adjectives
    adj1 = choice(adjective)
    adj2 = choice(adjective)
    adj3 = choice(adjective)
    while adj1 == adj2:
        adj2 = choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adjective)

    # Pull two different prepositions
    prep1 = choice(preposition)
    prep2 = choice(preposition)
    while prep1 == prep2:
        prep2 = choice(preposition)

    # Pull one adverb
    adv1 = choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # add lines to poem
    poem = f"{article} {adj1} {n1}\n\n"
    poem = poem + f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}\n"
    poem = poem + f"{adv1}, the {n1} {v2}\n"
    poem = poem + f"the {n2} {v3} {prep2} a {adj3} {n3}"

    return poem


print(make_poem())
