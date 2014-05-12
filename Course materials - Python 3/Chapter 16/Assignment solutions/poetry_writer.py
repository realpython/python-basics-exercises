# 12.2 poetry_writer.py
# Create random poems based on GUI input and save the output to files

from Tkinter import *
import tkFileDialog
from random import choice

def checkUnique(wordList):
    '''check that all items in a list are unique and return True or False'''
    uniqueWords = []
    for word in wordList:
        if word not in uniqueWords:
            uniqueWords.append(word)
    return len(wordList)==len(uniqueWords)

def makePoem():
    '''create a randomly generated poem, returned as a multi-line string'''
    
    # split the user input into lists
    noun = entryNoun.get().split(",")
    verb = entryVerb.get().split(",")
    adjective = entryAdj.get().split(",")
    adverb = entryAdv.get().split(",")
    preposition = entryPrep.get().split(",")

    # make sure that all lists consist of unique words
    if not (checkUnique(noun) and checkUnique(verb) and checkUnique(adjective)
            and checkUnique(adverb) and checkUnique(preposition)):
        resultPoem.config(text="Please do not enter duplicate words.")
        return
    
    # make sure that we got enough words from the user to make a poem
    if len(noun)<3 or len(verb)<3 or len(adjective)<3 or len(preposition)<2 or len(adverb)<1:
        resultPoem.config(text="Did you think you could get away that easily?\n\
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

    if "aeiou".find(adj1[0]) != -1: # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # put it all together into a poem
    poem = "{} {} {}\n\n".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}\n".format(article, adj1, n1, v1, prep1, adj2, n2)
    poem = poem + "{}, the {} {}\n".format(adv1, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)

    # place the resulting poem into the label 
    resultPoem.config(text=poem)


# create the application window and add a Frame
window = Tk()
window.title("Make your own poem!")
frame = Frame()
frame.grid(padx=5, pady=5) # pad top and left of frame 5 pixels before grid

# create and add text labels for text entry boxes
labelDirections = Label(frame, text="Enter your favorite words, separated by commas:")
labelDirections.grid(row=1, column=1, sticky=S+W, columnspan=2)
labelNoun = Label(frame, text="Nouns:")
labelNoun.grid(row=2, column=1, sticky=S+E)
labelVerb = Label(frame, text="Verbs:")
labelVerb.grid(row=3, column=1, sticky=S+E)
labelAdj = Label(frame, text="Adjectives:")
labelAdj.grid(row=4, column=1, sticky=S+E)
labelPrep = Label(frame, text="Prepositions:")
labelPrep.grid(row=5, column=1, sticky=S+E)
labelAdv = Label(frame, text="Adverbs:")
labelAdv.grid(row=6, column=1, sticky=S+E)

# create and add space for user entry of text
entryNoun = Entry(frame, width=80)
entryNoun.grid(row=2, column=2)
entryVerb = Entry(frame, width=80)
entryVerb.grid(row=3, column=2)
entryAdj = Entry(frame, width=80)
entryAdj.grid(row=4, column=2)
entryPrep = Entry(frame, width=80)
entryPrep.grid(row=5, column=2)
entryAdv = Entry(frame, width=80)
entryAdv.grid(row=6, column=2)

# create and add 'Create poem' button
btnCreate = Button(frame, text="Create your poem", command=makePoem)
btnCreate.grid(row=7, column=1, columnspan=2)

# create label into which to output the poem
resultPoem = Label(frame)
resultPoem.grid(row=9, column=1, rowspan=5, columnspan=2)

# function to save the poem displayed in the output box into a text file
def saveFile():
    typeList = [("Text files", "*.txt")]
    fileName = tkFileDialog.asksaveasfilename(filetypes=typeList,
                                              defaultextension=".txt")
    print fileName
    if fileName != "": # save file if user entered a file name
        outputFile = open(fileName, "w")
        outputFile.writelines(resultPoem.cget("text"))
        outputFile.close()

# create and add 'Save your poem' button
btnSave = Button(frame, text="Save your poem", command=saveFile)
btnSave.grid(row=15, column=1, columnspan=2)

mainloop() # start the application



