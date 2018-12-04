# 17.6 - Challenge: Return of the Poet
# Solution to challenge

import tkinter as tk
import random


def check_unique(word_list):
    """check that all items in a list are unique and return True or False"""
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return len(word_list) == len(unique_words)


def make_poem():
    """create a randomly generated poem, returned as a multi-line string"""

    # split the user input into lists
    noun = entry_noun.get().split(",")
    verb = entry_verb.get().split(",")
    adjective = entry_adj.get().split(",")
    adverb = entry_adv.get().split(",")
    preposition = entry_prep.get().split(",")

    # make sure that all lists consist of unique words
    if not (
        check_unique(noun)
        and check_unique(verb)
        and check_unique(adjective)
        and check_unique(adverb)
        and check_unique(preposition)
    ):
        result_poem.config(text="Please do not enter duplicate words.")
        return

    # make sure that we got enough words from the user to make a poem
    if (
        len(noun) < 3
        or len(verb) < 3
        or len(adjective) < 3
        or len(preposition) < 2
        or len(adverb) < 1
    ):
        result_poem.config(
            text="Did you think you could get away that easily?\n\
            Enter at least three nouns, three verbs, three adjectives, \
            two prepositions and an adverb!"
        )
        return

    # otherwise, we can go ahead with generating a poem:

    # pull three nouns randomly
    n1 = random.choice(noun)
    n2 = random.choice(noun)
    n3 = random.choice(noun)

    # make sure that all the nouns are different
    while n1 == n2:
        n2 = random.choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = random.choice(noun)

    # pull three different verbs
    v1 = random.choice(verb)
    v2 = random.choice(verb)
    v3 = random.choice(verb)
    while v1 == v2:
        v2 = random.choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verb)

    # pull three different adjectives
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)
    while adj1 == adj2:
        adj2 = random.choice(adjective)
    while n1 == n3 or n2 == n3:
        adj3 = random.choice(adjective)

    # pull two different prepositions
    prep1 = random.choice(preposition)
    prep2 = random.choice(preposition)
    while prep1 == prep2:
        prep2 = random.choice(preposition)

    # pull one adverb
    adv1 = random.choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # put it all together into a poem
    poem = f"{article} {adj1} {n1}\n\n"
    poem = poem + f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}\n"
    poem = poem + f"{adv1}, the {n1} {v2}\n"
    poem = poem + f"the {n2} {v3} {prep2} a {adj3} {n3}"

    # place the resulting poem into the label
    result_poem.config(text=poem)


# create the application window and add a Frame
window = tk.Tk()
window.title("Make your own poem!")
frame = tk.Frame()
frame.grid(padx=5, pady=5)  # pad top and left of frame 5 pixels before grid

# create and add text labels for text entry boxes
label_directions = tk.Label(
    frame, text="Enter your favorite words, separated by commas:"
)
label_directions.grid(row=1, column=1, sticky=tk.S + tk.E, columnspan=2)
label_noun = tk.Label(frame, text="Nouns:")
label_noun.grid(row=2, column=1, sticky=tk.S + tk.E)
label_verb = tk.Label(frame, text="Verbs:")
label_verb.grid(row=3, column=1, sticky=tk.S + tk.E)
label_adj = tk.Label(frame, text="Adjectives:")
label_adj.grid(row=4, column=1, sticky=tk.S + tk.E)
label_prep = tk.Label(frame, text="Prepositions:")
label_prep.grid(row=5, column=1, sticky=tk.S + tk.E)
label_adv = tk.Label(frame, text="Adverbs:")
label_adv.grid(row=6, column=1, sticky=tk.S + tk.E)

# create and add space for user entry of text
entry_noun = tk.Entry(frame, width=80)
entry_noun.grid(row=2, column=2)
entry_verb = tk.Entry(frame, width=80)
entry_verb.grid(row=3, column=2)
entry_adj = tk.Entry(frame, width=80)
entry_adj.grid(row=4, column=2)
entry_prep = tk.Entry(frame, width=80)
entry_prep.grid(row=5, column=2)
entry_adv = tk.Entry(frame, width=80)
entry_adv.grid(row=6, column=2)

# create and add 'Create poem' button
btn_create = tk.Button(frame, text="Create your poem", command=make_poem)
btn_create.grid(row=7, column=1, columnspan=2)

# create label into which to output the poem
result_poem = tk.Label(frame)
result_poem.grid(row=9, column=1, rowspan=5, columnspan=2)


# function to save the poem displayed in the output box into a text file
def save_file():
    type_list = [("Text files", "*.txt")]
    file_name = tk.filedialog.asksaveasfilename(
        filetypes=type_list, defaultextension="*.txt"
    )
    print(file_name)
    if file_name != "":  # save file if user entered a file name
        output_file = open(file_name, "w")
        output_file.writelines(result_poem.cget("text"))
        output_file.close()


# create and add 'Save your poem' button
btn_save = tk.Button(frame, text="Save your poem", command=save_file)
btn_save.grid(row=15, column=1, columnspan=2)

window.mainloop()  # start the application
