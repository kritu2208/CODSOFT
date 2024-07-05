from tkinter import *
import csv
import random, string
from tkinter import messagebox
import pyperclip
import json

#---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    # password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    characters = string.ascii_letters + string.digits + string.punctuation

    # password_list = password_symbols+password_numbers+password_letters
    # random.shuffle(password_list)
    # password = "".join(password_list)
    length = int(desired_length.get())
    password=""

    for index in range(length):
        password = password + random.choice(characters)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column = 2, row =1)



def save():
    website= web_entry.get()
    username= username_entry.get()
    password=password_entry.get()

    new_data = {website:{
        "email": username,
        "password":password
    }}

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file)
        finally:
            web_entry.delete(0,END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
E_username_label = Label(text="Email/Username:")
E_username_label.grid(column=1, row=3)
length_label = Label(text="Desired password length")
length_label.grid(column=1, row=4)
Password_label = Label(text="Password:")
Password_label.grid(column=1, row=5)



#entries
web_entry = Entry(width=52)
web_entry.grid(column=2, row=2, columnspan=2)
web_entry.focus()
username_entry= Entry(width=52)
username_entry.grid(column=2, row=3, columnspan=2)
username_entry.insert(0, "@gmail.com")
desired_length = Entry(width=33)
desired_length.grid(column=2, row=4)
password_entry = Entry(width=33)
password_entry.grid(column=2, row=5)


#buttons
gen_psswrd=Button(text="Generate Password", command=generate)
gen_psswrd.grid(column=3, row=5)
add_button=Button(text="Add", width=44, command=save)
add_button.grid(column=2, row=6, columnspan =2)

window.mainloop()