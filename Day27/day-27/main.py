from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=2)

# New Button
new_button = Button(text="New Button")
new_button.grid(column=3, row=0)


window.mainloop()