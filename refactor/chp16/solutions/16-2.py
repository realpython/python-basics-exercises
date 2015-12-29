# 16.2 review exercises

# Create a button that takes on the value in an entry box


from tkinter import *


def button_clicked():
    ''' sets the button text to the text in the entry box '''
    button.config(text=entry.get())

window = Tk()
# Create and add button
button = Button(text="   ", command=button_clicked)
button.grid(row=1, column=1)
# Create and add space for user entry of text
entry = Entry(width=10)
entry.grid(row=1, column=2)

window.mainloop()
