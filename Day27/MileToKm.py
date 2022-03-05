import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 200, height = 200)
window.config(padx=40, pady=40, bg="white")


miles_input = tkinter.Entry(width=10, font=("Arial", 18, "bold"))
miles_input.insert(tkinter.END, string="0")
miles_input.config(justify="center", width=7)
miles_input.grid(row = 0, column = 1)


class Label:
    def __init__(self, **kwargs): 
        self.text = kwargs["text"]
        self.row = kwargs["row"]
        self.column = kwargs["column"]
        self.label = tkinter.Label(text=f"{self.text}", font=("Arial", 18, "bold"))
        self.label.config(bg="white", padx = 10, pady = 10)
        self.label.grid(row = self.row, column = self.column)

mile_label = Label(text = "Miles", row = 0, column = 2)
is_equal_label = Label(text = "is equal to", row = 1, column = 0)
mile_to_km_label = Label(text = "0", row = 1, column = 1)
km_label = Label(text = "Km", row = 1, column = 2)

def miles_to_km():
    miles = float(miles_input.get())
    miles_in_km = str(round(miles*1.60934, 2))
    mile_to_km_label.label.config(text = miles_in_km)


calculate = tkinter.Button(text = "Calculate", command=miles_to_km)
calculate.grid(row = 2, column = 1)



window.mainloop()