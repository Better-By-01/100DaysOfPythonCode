from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)           # to cancel the timer we set previously
                                         # it stops to continue further
    canvas.itemconfigure(timer_text, text="00:00")
    timer_label.config(text = "Timer")
    check_label.config(text="")
    global reps
    reps = 0
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = math.floor(count/60)
    sec = count%60

    # Python is a dynamically typed language. This means that the Python interpreter does 
    # type checking only as code runs, and the type of a variable is allowed to change over its lifetime.

    # Dynamic typing: change in variables data type by change in content of that variable
    # a = 3             # here a is int
    # a = "Hello"       # here a becomes str

    if int(sec/10) == 0:     # i.e. if second is one digit
    # or
    # if sec < 10:
        sec = f"0{sec}"
    if int(min/10) == 0:    
        min = f"0{min}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}") 
    if count > 0:
        # after - execute a command after a time delay
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)

# Canvas widget
# it allows to layer one thing on top of the other

canvas = Canvas(width=205, height=227, bg=YELLOW, highlightthickness=0)                 # highlightthickness = 0 is for removing the border line
tomato_img = PhotoImage(file="./Day28/tomato.png")
canvas.create_image(102,115, image=tomato_img)                                          # x value almost 1/2*width lly for y as 1/2*height
timer_text = canvas.create_text(103,135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row = 1, column = 1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(row = 0, column = 1)


start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg="white", highlightthickness = 0)
start_button.config(command=start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12,"bold"),  bg = "white", command = reset_timer, highlightthickness = 0)
reset_button.grid(row = 2, column = 2)


check_label = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row = 3, column = 1)

window.mainloop()                   # this makes the GUI event driven
