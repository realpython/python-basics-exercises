import tkinter as tk

# Creating a window with a title
window = tk.Tk()
window.title("Address Entry Form")

# List of fields we want to have in our form
fields = ["First Name:",
          "Last Name:",
          "Address Line1:",
          "Address Line2:",
          "City:",
          "State/Province:",
          "Postal Code:",
          "Country:"]

# The top frame contains the fields and their entry widgets
top_frame = tk.Frame(relief=tk.SUNKEN, master = window)
top_frame.pack()

# We are going to use a 2 columns grid to place our widgets
# We initialise the current row variable of our grid
current_top_frame_row = 0

for field in fields:
    # For each field we create a label and entry widget
    label = tk.Label(text=field, master=top_frame)
    entry = tk.Entry(width=50, master=top_frame)
    # We place them in the current row of our grid
    label.grid(row=current_top_frame_row, column=0, sticky=tk.E)
    entry.grid(row=current_top_frame_row, column=1)
    # We increment the current line for the next field
    current_top_frame_row += 1

# Creating the bottom frame that contains
# the Submit & Clear buttons
bot_frame = tk.Frame(master=window)
bot_frame.pack(fill=tk.X, ipadx=5, ipady=5)
choices = ["Cancel",
           "Submit"]

for choice in choices:
    # Create the button and pack it to the right side
    button = tk.Button(text=choice, relief=tk.RAISED, master=bot_frame)
    button.pack(side=tk.RIGHT, padx=5, ipadx=10)
    
# Start the application
window.mainloop()
