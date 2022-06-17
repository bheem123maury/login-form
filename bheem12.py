from tkinter import *
from functools import partial


def user_credential(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())

#window

tkWindow = Tk()
tkWindow.title("Login Form")
tkWindow.geometry("300x250")


#Creating layout of login form

Label(tkWindow, text="Please enter details below", width="300", bg="orange",fg="white").pack()

#username label and text entry box

usernameLabel = Label(tkWindow, text="Username *").place(x=20,y=40)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=90,y=42)  

#password label and password entry box

passwordLabel = Label(tkWindow,text="Password *").place(x=20,y=80)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=90,y=82)  

user_credential = partial(user_credential, username, password)

#login button

loginButton = Button(tkWindow, text="Login", width=10, height=1, bg="orange", command=user_credential).place(x=105,y=130)  

tkWindow.mainloop()