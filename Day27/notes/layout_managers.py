# Layout manager: pack(), place() and grid()

import tkinter

# Window
window = tkinter.Tk() 
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# adding the padding
window.config(padx=50, pady=50)         # and the same can be done for individual widgets


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
# my_label.pack(side="left")                         
# my_label.place(x=0,y=100)             # upper left corner is the initial point (0,0)
my_label.grid(column=0, row =  0)       # it's position is relative to other components
                                        # like if we change 0, 0 to 5, 5 it will still be like row = 0, col = 0



# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row = 1, column = 1)


new_button = tkinter.Button(text="New Button")
new_button.grid(row = 0, column = 2)


# Entry
input = tkinter.Entry()
print(input.get())
# input.pack()
input.grid(row = 2, column = 3)


window.mainloop()