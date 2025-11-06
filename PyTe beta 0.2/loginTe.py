from tkinter import *
import json

users_file = 'mainusers.json'


def login():
    username = text.get()
    password = text2.get()

    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    if username in users and users[username] == password:
        label_status.config(text="Login successful!", fg="green")
        window.after(1500, window.destroy)
    else:
        label_status.config(text="Invalid credentials, try again!", fg="red")


def save_user(username, password, status_label, register_window):
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    if username and password:
        users[username] = password
        with open(users_file, 'w') as file:
            json.dump(users, file, indent=4)

        status_label.config(text="Registration successful!", fg="green")
        register_window.after(1500, register_window.destroy)
    else:
        status_label.config(text="Please fill in all fields!", fg="red")


def open_register():
    register_window = Toplevel(window)
    register_window.title("Register")
    register_window.geometry('420x300')

    Label(register_window, text="Username:").pack()
    entry_username = Entry(register_window)
    entry_username.pack()

    Label(register_window, text="Password:").pack()
    entry_password = Entry(register_window)
    entry_password.pack()

    status_label = Label(register_window, text="", font=("Arial", 10))
    status_label.pack()

    Button(register_window, text="Submit",
           command=lambda: save_user(entry_username.get(), entry_password.get(), status_label, register_window)).pack(pady=10)


window = Tk()
window.title('PyTe beta 0.2')
window.geometry('1180x670')

Label(window, text='PyTe beta 0.2', font=('Arial', 40)).pack(pady=100)

Label(window, text='Username', font=('Arial', 9)).pack()
text = Entry(window, justify="center", width=20, font=('Arial', 15))
text.pack()

Label(window, text='Password', font=('Arial', 9)).pack()
text2 = Entry(window, justify="center", width=20, font=('Arial', 15), show='*')
text2.pack()

label_status = Label(window, text="", font=("Arial", 12))
label_status.pack()

Button(window, text='Enter', width=20, height=1, font=('Arial', 13), command=login).pack(pady=40)
Button(window, text="Don't have an account?\nRegister here", command=open_register).pack(pady=14, side='left', padx=50)

window.mainloop()