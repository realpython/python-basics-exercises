# 17.4 - Control Layout With Geometry Managers
# Review Exercise #2

# NOTE: The first exercise in this section is instructional and does
# not require a solution to be shown here. For this reason, only the
# solution to the second exercise is presented.

import tkinter as tk


# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# Create a new frame `form_frame` to contain the Label
# and Entry widgets for entering address information.
form_frame = tk.Frame()
# Give the frame a sunken border effect
form_frame["relief"] = tk.SUNKEN
form_frame["borderwidth"] = 3
# Pack the frame into the window
form_frame.pack()

# Create the Label and Entry widgets for "First Name"
fname_label = tk.Label(master=form_frame)
fname_label["text"] = "First Name:"
fname_entry = tk.Entry(master=form_frame)
fname_entry["width"] = 50
# Use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the
# first row of the grid
fname_label.grid(row=0, column=0, sticky=tk.E)
fname_entry.grid(row=0, column=1)

# Create the Label and Entry widgets for "Last Name"
lname_label = tk.Label(master=form_frame)
lname_label["text"] = "Last Name:"
lname_entry = tk.Entry(master=form_frame)
lname_entry["width"] = 50
# Place the widgets in the second row of the grid
lname_label.grid(row=1, column=0, sticky=tk.E)
lname_entry.grid(row=1, column=1)

# Create the Label and Entry widgets for "Address Line 1"
address1_entry_label = tk.Label(master=form_frame)
address1_entry_label["text"] = "Address Line 1:"
address1_entry = tk.Entry(master=form_frame)
address1_entry["width"] = 50
# Place the widgets in the third row of the grid
address1_entry_label.grid(row=2, column=0, sticky=tk.E)
address1_entry.grid(row=2, column=1)

# Create the Label and Entry widgets for "Address Line 2"
address2_entry_label = tk.Label(master=form_frame)
address2_entry_label["text"] = "Address Line 2:"
address2_entry = tk.Entry(master=form_frame)
address2_entry["width"] = 50
# Place the widgets in the fourth row of the grid
address2_entry_label.grid(row=3, column=0, sticky=tk.E)
address2_entry.grid(row=3, column=1)
address2_entry["width"] = 50

# Create the Label and Entry widgets for "City"
city_entry_label = tk.Label(master=form_frame)
city_entry_label["text"] = "City:"
city_entry = tk.Entry(master=form_frame)
city_entry["width"] = 50
# Place the widgets in the fifth row of the grid
city_entry_label.grid(row=4, column=0, sticky=tk.E)
city_entry.grid(row=4, column=1)

# Create the Label and Entry widgets for "State/Province"
state_entry_label = tk.Label(master=form_frame)
state_entry_label["text"] = "State/Province:"
state_entry = tk.Entry(master=form_frame)
state_entry["width"] = 50
# Place the widgets in the sixth row of the grid
state_entry_label.grid(row=5, column=0, sticky=tk.E)
state_entry.grid(row=5, column=1)

# Create the Label and Entry widgets for "Postal Code"
postal_entry_label = tk.Label(master=form_frame)
postal_entry_label["text"] = "Postal Code:"
postal_entry = tk.Entry(master=form_frame)
postal_entry["width"] = 50
# Place the widgets in the seventh row of the grid
postal_entry_label.grid(row=6, column=0, sticky=tk.E)
postal_entry.grid(row=6, column=1)

# Create the Label and Entry widgets for "Country"
country_entry_label = tk.Label(master=form_frame)
country_entry_label["text"] = "Country:"
country_entry = tk.Entry(master=form_frame)
country_entry["width"] = 50
# Place the widgets in the eight row of the grid
country_entry_label.grid(row=7, column=0, sticky=tk.E)
country_entry.grid(row=7, column=1)

# Create a new frame `button_frame` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
button_frame = tk.Frame()
button_frame.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `button_frame`
submit_button = tk.Button(master=button_frame)
submit_button["text"] = "Submit"
submit_button.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `button_frame`
clear_button = tk.Button(master=button_frame)
clear_button["text"] = "Clear"
clear_button.pack(side=tk.RIGHT, ipadx=10)

# Start the application
window.mainloop()
