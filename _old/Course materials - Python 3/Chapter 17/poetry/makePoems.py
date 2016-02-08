import webapp2
from random import choice


def check_unique(word_list):
    '''check that all items in a list are unique and return True or False'''
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return len(word_list) == len(unique_words)


def make_poem(nouns, verbs, adjectives, adverbs, prepositions):
    '''create a randomly generated poem, returned as a multi-line string'''

    noun = nouns.split(",")
    verb = verbs.split(",")
    adjective = adjectives.split(",")
    adverb = adverbs.split(",")
    preposition = prepositions.split(",")

    # make sure that all lists consist of unique words
    if not (check_unique(noun) and check_unique(verb) and check_unique(adjective)
            and check_unique(adverb) and check_unique(preposition)):
        return "Please do not enter duplicate words."

    # check that we have enough words to make a poem
    if len(noun) < 3 or len(verb) < 3 or len(adjective) < 3 \
            or len(preposition) < 2 or len(adverb) < 1:
        return "Please enter more words..."

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
    while n1 == n3 or n2 == n3:
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
    poem = "{} {} {}<br /><br />".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}<br />".format(
        article, adj1, n1, v1, prep1, adj2, n2
    )
    poem = poem + "{}, the {} {}<br />".format(adv1, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)
    return poem


class MainPage(webapp2.RequestHandler):
    def get(self):
        nouns = self.request.get("nouns")
        verbs = self.request.get("verbs")
        adjectives = self.request.get("adjectives")
        adverbs = self.request.get("adverbs")
        prepositions = self.request.get("prepositions")
        poem = make_poem(nouns, verbs, adjectives, adverbs, prepositions)

        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Poem Generator</title></head>
            <body>
              <h1>Generate a random poem!</h1>
              (Enter at least three nouns, three verbs, three adjectives, two prepositions and an adverb.)
              <br /><br />
              Enter possible words for each part of speech, separated by commas:<br />
              <form action="/" method="get">
                Nouns: <input type="text" name="nouns" value={}><br />
                Verbs: <input type="text" name="verbs" value={}><br />
                Adjectives: <input type="text" name="adjectives" value={}><br />
                Adverbs: <input type="text" name="adverbs" value={}><br />
                Prepositions: <input type="text" name="prepositions" value={}><br />
                <input type="submit" value="Generate poem!"><br /><br />
                <p align="center">{}</p>
              </form>
            </body>
          </html>""".format(nouns, verbs, adjectives, adverbs, prepositions, poem))

routes = [('/', MainPage)]
my_app = webapp2.WSGIApplication(routes, debug=True)
