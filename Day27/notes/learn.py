# Tkinter
import tkinter

# Creating windows
window = tkinter.Tk() 

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack()                         # by default show the label onto the screen and center it

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")

# button = tkinter.Button(text = "Click Me", command=button_clicked)          # command here is a click event
# button.pack()

# Entry

def input_entered():
    entered_text = input.get()                            # returns the input as string
    my_label.config(text=entered_text)

input = tkinter.Entry()
input.insert(tkinter.END, string="Enter something")

button = tkinter.Button(text = "Click Me", command=input_entered) 
button.pack()

input.pack()

# Text: Multiline text Box
text = tkinter.Text(height=5, width=30)                             # here height defines the no. of lines inside the text box
text.focus()                                                        # puts cursor inside textbox
text.insert(tkinter.END, "Example of multi-line text entry.")       
print(text.get("1.0", tkinter.END))                                 # get current value in textbox at line 1, character 0
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# called with current scale value
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # prints 1 if on button checked, otherwise 0.
    print(checked_state.get())

# A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well
checked_state = tkinter.IntVar()        # variable to hold on to checked state, 0 for off, 1 for no.

checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)

checkbutton.pack()


# Radiobutton

def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

fruits = ["Apple", "Pear", "Orange", "Banana"]
listbox = tkinter.Listbox(height=4)
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()                       # for keep the window on the screen and listen to how the user interacts