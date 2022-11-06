from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.append("".join([random.choice(letters) for _ in range(nr_letters)]))

    password_list.append("".join([random.choice(symbols) for _ in range(nr_symbols)]))

    password_list.append("".join([random.choice(numbers) for _ in range(nr_numbers)]))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += str(char)

    pyperclip.copy(password)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(message="Oops", detail="Don't leave any fields blank!")
        return

    line = website + " | " + email + " | " + password + "\n"

    is_ok = messagebox.askokcancel(message=website, detail=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        data = open("data.txt", "a")
        data.write(line)
        data.close()

        web_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(bg="white", text="Website:", fg="black")
web_label.grid(row=1, column=0)
email_label = Label(bg="white", text="Email/Username:", fg="black")
email_label.grid(row=2, column=0)
password_label = Label(bg="white", text="Password:", fg="black")
password_label.grid(row=3, column=0)

# Entries
web_entry = Entry()
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
web_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "jeligooch@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(width=35, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()