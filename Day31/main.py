from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE_PATH ="/home/better-by-01/100DaysOfPythonCode/Day31/data/french_words.csv"
TO_LEARN_FILE ="/home/better-by-01/100DaysOfPythonCode/Day31/data/words_to_learn.csv"
IMAGES_FILE_PATH = "/home/better-by-01/100DaysOfPythonCode/Day31/images/"

current_card={}
data_list_dict = {}

#----------------------------------------------- TITLE AND WORD ---------------------------------------------------------#
try:
    data_list_dict = pandas.read_csv(TO_LEARN_FILE)
except FileNotFoundError:
    data = pandas.read_csv(DATA_FILE_PATH)
    data_list_dict = data.to_dict(orient="records")
else:
    data = pandas.read_csv(TO_LEARN_FILE)
    data_list_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    current_card = random.choice(data_list_dict)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    data_list_dict.remove(current_card)
    data = pandas.DataFrame(data_list_dict)
    data.to_csv(TO_LEARN_FILE, index=False)
    next_card()

#------------------------------------------------ UI SETUP --------------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=f"{IMAGES_FILE_PATH}card_front.png")
card_back_img = PhotoImage(file=f"{IMAGES_FILE_PATH}card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)         # x, y, image
card_title = canvas.create_text(400, 150, text="Title", font=("Times New Roman", 40,"italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Times New Roman", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file=f"{IMAGES_FILE_PATH}wrong.png")
wrong_button = Button(image=wrong_img, border = 0, highlightthickness=0)
wrong_button.config(command=next_card)
wrong_button.grid(row=1, column = 0)

right_img = PhotoImage(file=f"{IMAGES_FILE_PATH}right.png")
right_button = Button(image=right_img, border = 0, highlightthickness=0)
right_button.config(command=is_known)
right_button.grid(row=1, column = 1)

next_card()

window.mainloop()