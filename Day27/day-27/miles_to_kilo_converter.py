from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_str = "{:.2f}".format(km)
    kilometers_label.config(text=km_str)


# Miles Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(0, "0")

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)

kilometers_label = Label(text="0", font=("Arial", 24, "bold"))
kilometers_label.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()