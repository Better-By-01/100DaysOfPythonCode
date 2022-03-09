from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FILE_PATH = "/home/better-by-01/100DaysOfPythonCode/Day30/improved_pass_manager/data.json" 

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

    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data_dict = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty")

    else:
        try:
            with open(FILE_PATH, "r") as datafile:
                # json.dump(new_data_dict, datafile, indent=4)              # what to dump , where to dump

                # Reading the old data
                data = json.load(datafile)

        except FileNotFoundError:
            with open(FILE_PATH, "w") as data_file:
                json.dump(new_data_dict, data_file, indent=4)
        
        else: 
            # Updating old with new data
            data.update(new_data_dict) 

            with open(FILE_PATH, "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            # clearing the entries
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ----------------------------- SEARCH -------------------------------- #
def find_password():
    website = website_input.get().lower()
    if len(website) == 0:
        messagebox.showerror("Oops", "Please don't leave the field empty !")
    else:
        try:
            with open(FILE_PATH, "r") as data_file:
                content = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror("Oops", "No Data File Found")
        else:
            try:
                with open(FILE_PATH, "r") as datafile:
                    content = json.load(datafile)
                    messagebox.showinfo(website.capitalize(), f"Email: {content[website]['email']}\nPassword: {content[website]['password']}")

            except KeyError:
                messagebox.showerror(website.capitalize(), f"No details for the {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="/home/better-by-01/100DaysOfPythonCode/Day30/improved_pass_manager/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


website_input = Entry(width=28)
website_input.insert(END, string="")
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=48)
email_input.insert(END, string="asp8384@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=28)
password_input.insert(END, string="")
password_input.grid(row=3, column=1)

search_button = Button(text="Search", bg="white", command=find_password, width=15)
search_button.grid(row=1, column=2)

gen_pass_button = Button(text="Generate Password", bg="white", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()