from tkinter import *

window = Tk()
window.config(padx=10, pady=10)

# Colspace attribute in grid

r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

# both width has been doubled and columnspan attribute has been added
b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)



# tkinter standard dialogs (pop-ups)
# like messagebox.showinfo(title="Title", message="Message")

# Using Pyperclip for getting the hold of a text in clipboard
# it's a python module for copy and past clipboard functions.



window.mainloop()