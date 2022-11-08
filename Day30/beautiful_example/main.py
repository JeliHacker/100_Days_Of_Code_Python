from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, choice, shuffle
import json

# ----------------------------Variables------------------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# --------------------------------Security check------------------------------------#

def intro(is_first):
    # Variables
    pass_text = "Password"
    note_text = ""
    btn_text = "Check"
    if is_first:
        pass_text = "Choose Password: "
        note_text = "This password is required to unlock this app.\n\nNote:1)Remember " \
                    "Password\n         2)Choose strong Password\nConform Password?"
        btn_text = "Save"
    # Window
    intro_win = Tk()
    intro_win.title("Setup")
    intro_win.config(bg="light blue")
    intro_win.geometry("370x360")

    # Canvas
    logo_canvas = Canvas(bg="light blue", highlightthickness=0)
    intro_img = PhotoImage(file="image.png")
    logo_canvas.create_image(180, 180, image=intro_img)
    logo_canvas.place(x=0, y=0)

    # Labels
    name = Label(text="Light Blue Security")
    name.config(bg="light blue", fg="orange", font=("aerial", 20, "bold"))
    name.place(x=60, y=10)

    note_info = Label(text=note_text)
    note_info.config(bg="light blue", fg="red", font=("aerial", 8, "bold"))
    note_info.place(x=3, y=340)

    pass_info = Label(text=pass_text)
    pass_info.config(bg="light blue", fg="green", font=("aerial", 10, "bold"))
    pass_info.place(x=5, y=280)

    # TextField
    entry = Entry(width=30)
    entry.place(x=130, y=280)

    # Save pass

    def store_pass():
        response = messagebox.askyesno(title="Conform Password",
                                       message=note_text)
        if response:
            update_info = {"password": entry.get()}
            print(len(update_info["password"]))
            if len(update_info["password"]) > 0:
                if update_info["password"][0] != " ":
                    with open("appdata.json") as app_info:
                        data = json.load(app_info)
                        data.update(update_info)
                    with open("appdata.json", 'w') as app_info:
                        print(data["password"])
                        data["password"] = entry.get()
                        json.dump(data, app_info)
                    entry.delete(0, END)
                    intro_win.destroy()

    def security_chek():
        with open("appdata.json") as file:
            password = json.load(file)["password"]
            if entry.get() == password:
                intro_win.destroy()
            else:
                messagebox.showwarning(title="Bad Password.", message="The Password you entered was not correct one.")
                quit()

    # Button
    if is_first:
        save_btn = Button(text=btn_text, width=15, command=store_pass)
    else:
        save_btn = Button(text=btn_text, width=15, command=security_chek)
        print("Passed")
    save_btn.place(x=160, y=310)

    intro_win.mainloop()


with open("appdata.json") as appdata:
    data = json.load(appdata)
    is_first_time = data["is_first_time"]
if is_first_time == "True":
    intro(True)
    with open("appdata.json") as appdata:
        data = json.load(appdata)
    data["is_first_time"] = "False"
    with open("appdata.json", 'w') as file_appdata:
        json.dump(data, file_appdata)
else:
    intro(False)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError or json.decoder.JSONDecodeError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                pass
            else:
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def put_default():
    try:
        with open("data.json") as file:
            data = json.load(file)
            if len(data) != 0:
                for website in data:
                    email_entry.delete(0, END)
                    email_entry.insert(END, data[website]["email"])
    except FileNotFoundError or json.decoder.JSONDecodeError:
        email_entry.delete(0, END)
        email_entry.insert(END, "example@gmail.com")


# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) != 0:
        try:
            with open("data.json") as file:
                data = json.load(file)
            password = data[website]["password"]
            email = data[website]["email"]
        except FileNotFoundError:
            messagebox.showwarning("File not found Error", "No data file found.\n\nSolution: Please add some data and "
                                                           "save passwords to search.")
        except KeyError:
            if website[0] == " ":
                messagebox.showerror("Error", "Please enter valid data to search.\nSearch with exact website name "
                                              "without any spaces.")
            else:
                messagebox.showerror("Error", "The website you searched for is not added to our DataBase.")
        else:
            pyperclip.copy(password)
            message = f"Email/Username: {email}\nPassword: {password}\n\nNote: Your password is copied to clipboard."
            messagebox.showinfo(website, message)


# ----------------------------Menu Functions------------------------------- #
def format_data(new_window):
    pass_buttons = []
    passwords = []
    emails = []
    websites = []
    web_y = 30
    em_y = 30
    pas_y = 30
    pass_btn_width = 0
    try:
        with open("data.json") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        if_no = Label(new_window, text="No Saved Data or Passwords found\nAdd Passwords to view them.", bg="light blue")
        if_no.place(x=110, y=90)
    else:
        for website in data:
            websites.append(website)
            emails.append(data[website]["email"])
            passwords.append(data[website]["password"])
        for passw in passwords:
            if len(passw) > pass_btn_width:
                pass_btn_width = len(passw)
        for website in websites:
            websites_label = Label(new_window, text=website, bg="light blue")
            websites_label.place(x=10, y=web_y)
            web_y += 30
        for email in emails:
            emails_label = Label(new_window, text=email, bg="light blue")
            emails_label.place(x=150, y=em_y)
            em_y += 30

        def copy_pass(password_to_copy):
            pyperclip.copy(password_to_copy)

        for password in passwords:
            pas_button = Button(new_window, text=password, height=1, width=pass_btn_width, bg="light blue")
            pas_button.config(command=lambda password_arg=pas_button: copy_pass(password_arg.cget('text')))
            pas_button.place(x=300, y=pas_y)
            pas_y += 30
            pass_buttons.append(pas_button)

    new_window.mainloop()


def view_saved():
    new_window = Tk()
    new_window.geometry("450x200")
    new_window.config(bg="light blue")
    new_window.title("Saved Passwords")
    web_label = Label(new_window, text="Website", fg="red", font=("aerial", 10, "bold"), bg="light blue")
    web_label.place(x=10, y=10)
    email_user_label = Label(new_window, text="Email/Username", fg="red", font=("aerial", 10, "bold"), bg="light blue")
    email_user_label.place(x=150, y=10)
    pas_label = Label(new_window, text="Password", fg="red", font=("aerial", 10, "bold"), bg="light blue")
    pas_label.place(x=300, y=10)
    format_data(new_window)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="light blue")

# Canvas
canvas = Canvas(height=200, width=200, bg="light blue", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="light blue", font=("aerial", 10, "bold"), fg="red")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="light blue", font=("aerial", 10, "bold"), fg="red")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="light blue", font=("aerial", 10, "bold"), fg="red")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21, bg="light green", font=("aerial", 8, "bold"))
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=39, bg="light green", font=("aerial", 8, "bold"))
email_entry.grid(row=2, column=1, columnspan=2)
put_default()
password_entry = Entry(width=21, bg="light green", font=("aerial", 8, "bold"))
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search, bg=YELLOW)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Menu Bar
menu_bar = Menu(window)
options = Menu(menu_bar, tearoff=0)
options.add_command(label="Saved Passwords", command=view_saved)
options.add_command(label="Back")

options.add_separator()

options.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="Options", menu=options)
window.config(menu=menu_bar)
print(window.winfo_height(), window.winfo_width())

window.mainloop()