from tkinter import *

window = Tk()
window.title("Login System")
window.geometry("400x400")


def Login():
    login_text["text"] = user_entry.get()

text = Label(window, text= "Login System")
text.grid(column= 0,row = 0, padx = 5, pady= 5)

user_text = Label(window, text= "User:")
user_entry = Entry(window, width= 20)
user_text.grid(column = 1, row = 1)
user_entry.grid(column = 2, row = 1)



password_text = Label(window, text= "Password:")
password_entry = Entry(window, width= 20)
password_text.grid(column = 1, row = 2)
password_entry.grid(column = 2, row = 2)

login_button = Button(window, text="Login", width=10, command = Login)
login_button.grid(row = 4, column= 2)

login_text = Label(window, text="")
login_text.grid(row = 5, column= 2)

window.mainloop()