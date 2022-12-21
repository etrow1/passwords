import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.grid()

# Login Window
def openLogin():
    loginWindow = Toplevel(window)
    loginWindow.title("Login")
    loginWindow.grid()
    
    username = StringVar()
    password = StringVar()

    # get the username for login
    ttk.Label(loginWindow, text="Username").grid(column=0, row=0, sticky=W, pady=5, padx=5)
    ttk.Entry(loginWindow, textvariable=username).grid(column=1, row=0, padx=5)

    # get the password for login
    ttk.Label(loginWindow, text="Password").grid(column=0, row=1, sticky=W, pady=5, padx=5)
    ttk.Entry(loginWindow, textvariable=password, show="*").grid(column=1, row=1, padx=5)
            
    # when "login" button clicked, check to see if we have that login info in .csv file
    def log():
        with open("pswds.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)
            for col in reader:
                if col == [username.get(),password.get()]:
                    messagebox.showinfo(title="Login Successful", message="You have successfully logged in!")
                    return True
        messagebox.showinfo(title="Login Failed", message="Incorrect info. Please try again!")
        return False
    
    # button to login            
    ttk.Button(loginWindow, text="Login", command=log).grid(row=2, column=0,rowspan=1, columnspan=2, sticky=S, pady=10, padx=10)

# Register Window
def openRegister():
    registerWindow = Toplevel(window)
    registerWindow.title("Register")
    registerWindow.grid()
    
    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    # get the username for register
    ttk.Label(registerWindow, text="Username:").grid(column=0, row=0, sticky=E, pady=5)
    ttk.Entry(registerWindow, textvariable=username).grid(column=1, row=0, padx=5)

    # get the password for register
    ttk.Label(registerWindow, text="Password:").grid(column=0, row=1, sticky=E, pady=5)
    ttk.Entry(registerWindow, textvariable=password).grid(column=1, row=1, padx=5)

    # verify password for register
    ttk.Label(registerWindow, text="Verify Password:").grid(column=0, row=2, sticky=E, pady=5)
    ttk.Entry(registerWindow, textvariable=password1).grid(column=1, row=2, padx=5)

    # when "Register" button clicked, check to see if password was typed in 2 times, correctly. Then write to .csv file.
    def reg():
        with open("pswds.csv",  mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            if password.get() == password1.get():
                writer.writerow([username.get(),password.get()])
                messagebox.showinfo(title="Registration Successful", message=f"Welcome {username.get()}!")
                return True
        messagebox.showinfo(title="Incorrect info", message="Passwords do not match. Please try again!")
        return False
    
    # button to register
    ttk.Button(registerWindow, text="Register", command=reg).grid(row=3, column=0,rowspan=1, columnspan=2, sticky=S, pady=10, padx=10)

# main menu buttons
Label(window, text="Please select one below!", anchor=CENTER, font=("Arial", 20)).grid(column=0, row=0, columnspan=3, rowspan=1, sticky=N, pady=5)
Button(window, text="Login", command=openLogin, anchor=CENTER, font=("Arial", 12), cursor="hand2", activebackground="#bec3d1").grid(row=1, column=1, padx=5, pady=3)
Button(window, text="Register", command=openRegister, anchor=CENTER, font=("Arial", 12), cursor="hand2", activebackground="#bec3d1").grid(row=2, column=1, padx=5, pady=3)

window.mainloop()
