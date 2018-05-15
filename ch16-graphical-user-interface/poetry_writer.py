# chapter 15 poetry_writer.py
# Create random poems based on GUI input and save the output to files

from tkinter import *
from tkinter import filedialog
from random import choice


def check_unique(word_list):
    '''check that all items in a list are unique and return True or False'''
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return len(word_list) == len(unique_words)


def make_poem():
    '''create a randomly generated poem, returned as a multi-line string'''

    # split the user input into lists
    noun = entry_noun.get().split(",")
    verb = entry_verb.get().split(",")
    adjective = entry_adj.get().split(",")
    adverb = entry_adv.get().split(",")
    preposition = entry_prep.get().split(",")

    # make sure that all lists consist of unique words
    if not (check_unique(noun) and
            check_unique(verb) and
            check_unique(adjective) and
            check_unique(adverb) and check_unique(preposition)
            ):
        result_poem.config(text="Please do not enter duplicate words.")
        return

    # make sure that we got enough words from the user to make a poem
    if len(noun) < 3 or len(verb) < 3 or len(adjective) < 3 \
            or len(preposition) < 2 or len(adverb) < 1:
        result_poem.config(
            text="Did you think you could get away that easily?\n\
            Enter at least three nouns, three verbs, three adjectives, two prepositions and an adverb!")
        return

    # otherwise, we can go ahead with generating a poem:

    # pull three nouns randomly
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)

    # make sure that all the nouns are different
    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

    # pull three different verbs
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)

    # pull three different adjectives
    adj1 = choice(adjective)
    adj2 = choice(adjective)
    adj3 = choice(adjective)
    while adj1 == adj2:
        adj2 = choice(adjective)
    while n1 == n3 or n2 == n3:
        adj3 = choice(adjective)

    # pull two different prepositions
    prep1 = choice(preposition)
    prep2 = choice(preposition)
    while prep1 == prep2:
        prep2 = choice(preposition)

    # pull one adverb
    adv1 = choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # put it all together into a poem
    poem = "{} {} {}\n\n".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}\n".format(
        article, adj1, n1, v1, prep1, adj2, n2
    )
    poem = poem + "{}, the {} {}\n".format(adv1, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)

    # place the resulting poem into the label
    result_poem.config(text=poem)


# create the application window and add a Frame
window = Tk()
window.title("Make your own poem!")
frame = Frame()
frame.grid(padx=5, pady=5)  # pad top and left of frame 5 pixels before grid

# create and add text labels for text entry boxes
label_directions = Label(
    frame, text="Enter your favorite words, separated by commas:"
)
label_directions.grid(row=1, column=1, sticky=S + W, columnspan=2)
label_noun = Label(frame, text="Nouns:")
label_noun.grid(row=2, column=1, sticky=S + E)
label_verb = Label(frame, text="Verbs:")
label_verb.grid(row=3, column=1, sticky=S + E)
label_adj = Label(frame, text="Adjectives:")
label_adj.grid(row=4, column=1, sticky=S + E)
label_prep = Label(frame, text="Prepositions:")
label_prep.grid(row=5, column=1, sticky=S + E)
label_adv = Label(frame, text="Adverbs:")
label_adv.grid(row=6, column=1, sticky=S + E)

# create and add space for user entry of text
entry_noun = Entry(frame, width=80)
entry_noun.grid(row=2, column=2)
entry_verb = Entry(frame, width=80)
entry_verb.grid(row=3, column=2)
entry_adj = Entry(frame, width=80)
entry_adj.grid(row=4, column=2)
entry_prep = Entry(frame, width=80)
entry_prep.grid(row=5, column=2)
entry_adv = Entry(frame, width=80)
entry_adv.grid(row=6, column=2)

# create and add 'Create poem' button
btn_create = Button(frame, text="Create your poem", command=make_poem)
btn_create.grid(row=7, column=1, columnspan=2)

# create label into which to output the poem
result_poem = Label(frame)
result_poem.grid(row=9, column=1, rowspan=5, columnspan=2)


# function to save the poem displayed in the output box into a text file
def save_file():
    type_list = [("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(filetypes=type_list,
                                             defaultextension=".txt")
    print(file_name)
    if file_name != "":  # save file if user entered a file name
        output_file = open(file_name, "w")
        output_file.writelines(result_poem.cget("text"))
        output_file.close()

# create and add 'Save your poem' button
btn_save = Button(frame, text="Save your poem", command=save_file)
btn_save.grid(row=15, column=1, columnspan=2)

window.mainloop()  # start the application
