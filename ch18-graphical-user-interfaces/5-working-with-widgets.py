# 18.4 - Introduction to Tkinter
# Review exercises

import tkinter as tk


# Exercise 1 asks you to recreate all the windows in the chapter.
# The source code for each window can be found in the chapter text.


# Exercise 2
window = tk.Tk()
button = tk.Button(
    width=50, height=25, bg="white", fg="blue", text="Click here"
)
button.pack()
window.mainloop()


# Exercise 3
window = tk.Tk()
entry = tk.Entry(width=40)
entry.insert(0, "What is your name?")
entry.pack()
window.mainloop()
