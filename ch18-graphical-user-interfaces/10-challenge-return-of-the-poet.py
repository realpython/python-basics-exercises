# 18.10 - Challenge: Return of the Poet
# Solution to challenge

# Please note that there are many ways to solve this challenge. The code
# contained in this solution is just one way. If your solution is different,
# but works, then you did a great job!

import tkinter as tk
from tkinter import filedialog
import random


# Create the application window
window = tk.Tk()
window.title("Make your own poem!")

# Application Header Frame
header_frame = tk.Frame()
header_label = tk.Label(master=header_frame)
header_label["text"] = "Enter your favorite words, separated by commas."
header_label.pack()
header_frame.pack(padx=5, pady=5)

# Application Input Frame
input_frame = tk.Frame()
# Label widgets for text entry boxes
label_noun = tk.Label(input_frame, text="Nouns:")
label_verb = tk.Label(input_frame, text="Verbs:")
label_adj = tk.Label(input_frame, text="Adjectives:")
label_prep = tk.Label(input_frame, text="Prepositions:")
label_adv = tk.Label(input_frame, text="Adverbs:")
# Entry widgets for entering nouns, verbs, etc.
entry_noun = tk.Entry(input_frame, width=80)
entry_verb = tk.Entry(input_frame, width=80)
entry_adj = tk.Entry(input_frame, width=80)
entry_prep = tk.Entry(input_frame, width=80)
entry_adv = tk.Entry(input_frame, width=80)
# Add each label and entry widget to the input_frame using the .grid()
# geometry manager.
label_noun.grid(row=2, column=1, sticky=tk.E)
entry_noun.grid(row=2, column=2)
label_verb.grid(row=3, column=1, sticky=tk.E)
entry_verb.grid(row=3, column=2)
label_adj.grid(row=4, column=1, sticky=tk.E)
entry_adj.grid(row=4, column=2)
label_prep.grid(row=5, column=1, sticky=tk.E)
entry_prep.grid(row=5, column=2)
label_adv.grid(row=6, column=1, sticky=tk.E)
entry_adv.grid(row=6, column=2)
input_frame.pack(padx=5, pady=5)
# Button widget for generating a poem
generate_frame = tk.Frame(master=window)
generate_frame.pack(pady=10)
generate_button = tk.Button(generate_frame, text="Generate")
generate_button.pack()

# Application Result Frame
# Displays the generated poem
result_frame = tk.Frame(master=window)
result_frame["relief"] = tk.GROOVE
result_frame["borderwidth"] = 5
result_label = tk.Label(master=result_frame)
result_label["text"] = "Your poem:"
result_label.pack(pady=10)
result_poem = tk.Label(result_frame)
result_poem["text"] = "Press the 'Generate' button to display your poem."
result_poem.pack(padx=5)
save_button = tk.Button(result_frame, text="Save to file")
save_button.pack(pady=10)
result_frame.pack(fill=tk.X, padx=5, pady=5)


# Button command functions
def are_unique(word_list):
    """Check that all items in a list are unique and return True or False"""
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return len(word_list) == len(unique_words)


def generate_poem():
    """Generate a poem and assign it to the `result_poem` Label widget"""

    # Split the user input into lists
    noun = entry_noun.get().split(",")
    verb = entry_verb.get().split(",")
    adjective = entry_adj.get().split(",")
    adverb = entry_adv.get().split(",")
    preposition = entry_prep.get().split(",")

    # Make sure that all lists consist of unique words
    if not (
        are_unique(noun)
        and are_unique(verb)
        and are_unique(adjective)
        and are_unique(adverb)
        and are_unique(preposition)
    ):
        result_poem["text"] = "Please do not enter duplicate words."
        return

    # Make sure that we got enough words from the user to make a poem
    if (
        len(noun) < 3
        or len(verb) < 3
        or len(adjective) < 3
        or len(preposition) < 2
        or len(adverb) < 1
    ):
        result_poem["text"] = (
            "There was a problem with your input!\n"
            "Enter at least three nouns, three verbs, three adjectives, "
            "two prepositions and an adverb!"
        )
        return

    # Otherwise, we can go ahead with generating a poem:

    # Get three nouns randomly
    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    noun3 = random.choice(noun)

    # Make sure that all the nouns are different
    while noun1 == noun2:
        noun2 = random.choice(noun)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(noun)

    # Get three different verbs
    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    verb3 = random.choice(verb)
    while verb1 == verb2:
        verb2 = random.choice(verb)
    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(verb)

    # Get three different adjectives
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)
    while adj1 == adj2:
        adj2 = random.choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjective)

    # Get two different prepositions
    prep1 = random.choice(preposition)
    prep2 = random.choice(preposition)
    while prep1 == prep2:
        prep2 = random.choice(preposition)

    # Get one adverb
    adv1 = random.choice(adverb)

    if adj1[0] in "aeiou":  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    # Put it all together into a poem
    poem = f"{article} {adj1} {noun1}\n\n"
    poem = (
        poem + f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
    )
    poem = poem + f"{adv1}, the {noun1} {verb2}\n"
    poem = poem + f"the {noun2} {verb3} {prep2} a {adj3} {noun3}"

    # Place the resulting poem into the label
    result_poem["text"] = poem


def save_poem_to_file():
    """Save the poem displayed in the output box into a text file"""
    type_list = [("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(
        filetypes=type_list, defaultextension="*.txt"
    )
    # Save file if user entered a file name
    if file_name != "":
        with open(file_name, "w") as output_file:
            output_file.writelines(result_poem["text"])


# Assign the commands to the buttons
generate_button["command"] = generate_poem
save_button["command"] = save_poem_to_file

# Start the application
window.mainloop()
