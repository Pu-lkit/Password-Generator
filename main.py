from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice, randrange


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '<', '>', '?', '\'', ':', ';']
    password = []
    for i in range(5):
    	password.append(letters[randrange(len(letters))])
    for i in range(3):
    	password.append(numbers[randrange(len(numbers))])
    for i in range(3):
    	password.append(symbols[randrange(len(password))])
    shuffle(password)
    password = "".join(password)
    passw.insert(0, password)


def save():
    website = web.get()
    email = e_id.get()
    password = passw.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error!", message="An empty field detected")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it okay?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website is {website}\nYour Email-Id is {email}\nYour Password is {password}\n\n")
                passw.delete(0, END)
                web.delete(0, END)
                e_id.delete(0, END)


window = Tk()
window.geometry("900x550")
window.title("Password Generator")
window.config(padx=60, pady=60)

canvas = Canvas(width=300, height=250)
lock = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0, columnspan = 2)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(pady=10)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(pady=10)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(pady=10)

web = Entry(width=45, textvariable="He")
web.grid(column=1, row=1, columnspan=2)
web.insert(0, "MySite")
web.focus()

e_id = Entry(width=45)
e_id.grid(column=1, row=2, columnspan=2)
e_id.insert(0, "Email-id")

passw= Entry(width=22)
passw.grid(column=1, row=3)
passw.insert(0, "123456")

generate_password = Button(text="Generate Password", width=20, command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
