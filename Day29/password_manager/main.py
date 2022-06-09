from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 
            'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
            'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # OR
    password = "".join(password_list) 
    password_input.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=website, 
                            message=f"These are the details entered: \n\n Email: {email}\n Password: {password}\n\n Is it ok to save?")

        if is_ok:
            with open("./Day29/password_manager/data.txt", "a") as datafile:
                datafile.write(f"{website}\t|\t{email}\t|\t{password}\n")
                # clearing the entries
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="./Day29/password_manager/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


website_input = Entry(width=48)
website_input.insert(END, string="")
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=48)
email_input.insert(END, string="asp8384@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=28)
password_input.insert(END, string="")
password_input.grid(row=3, column=1)


gen_pass_button = Button(text="Generate Password", bg="white", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()