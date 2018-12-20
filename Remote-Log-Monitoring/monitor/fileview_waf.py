
# login and signup GUI


from tkinter import *
import tkinter
import os
import filewatch
creds = 'tempfile.temp'


def Signup():
    global passwordE
    global nameE
    global roots

    roots = Tk()
    roots.configure(background="lavender")
    roots.title('SignUp')
    # photo = tkinter.PhotoImage(file="Managed MonitoringConsole.gif")
    # w = tkinter.Label(roots, image=photo)
    # w.grid(row=0, column=1)
    Label(roots, text='Please SignUp To Continue\n', bg="lavender", font=("Helvetica", 16)).grid(row=1,column=1)
    Label(roots, text='New Username: ', bg="lavender", font=("Helvetica", 12)).grid(row=2, column=0, sticky=W)
    Label(roots, text='New Password: ', bg="lavender", font=("Helvetica", 12)).grid(row=3, column=0, sticky=W)

    nameE = Entry(roots)
    nameE.grid(row=2, column = 1)
    passwordE = Entry(roots, show='*')
    passwordE.grid(row=3, column=1)

    Button(roots, borderwidth = 1, text='Signup', command=FSSignup, font=("Helvetica", 10), fg='#a1dbcd' , bg= "#383a39").grid(column=2, sticky=W)
    roots.pack_slaves()
    roots.mainloop()


def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(passwordE.get())
        f.close()

    roots.destroy()
    Login()


def Login():
    global rootA
    global top
    rootA = Tk()
    creds = 'tempfile.temp'
    photo = tkinter.PhotoImage(file="Social-Media-Monitoring.gif")
    w = tkinter.Label(rootA, image=photo)
    w.pack(side = TOP)

    L1 = Label(rootA, text='Please Login To Continue\n',  font=("Helvetica", 16))
    L1.pack(side = TOP, anchor=W, fill=X)

    L2 = Label(rootA, text="Username", font=("Helvetica"), height=4)
    L2.pack(padx=3,pady=0)
    username_entry = Entry(rootA, bd=5)
    username_entry.pack(padx=4,pady=0)
    # username entry
    L2 = Label(rootA, text="Password", font=("Helvetica"), height=4)
    L2.pack(padx=3, pady=0)
    password_entry = Entry(rootA, bd=5)
    password_entry.pack(padx=4, pady=0)

    def trylogin():
        with open(creds) as f:
            data = f.readlines()
            uname = data[0].rstrip()
            pword = data[1].rstrip()
        if uname == username_entry.get() and pword == password_entry.get():
           Path()
        else:
            WrongInput()

    # when you press this button, trylogin is called

    button3 = Button(rootA, text='Delete User', fg='red', command=DelUser, font=("Helvetica", 10),  bg= "#383a39")
    button3.pack(side = RIGHT, padx=1)

    button2 = Button(rootA, text='Quit', command=rootA.quit, font=("Helvetica", 10), fg='#a1dbcd', bg="#383a39")
    button2.pack(side = RIGHT, padx=1)

    button = Button(rootA, text="Login", command=trylogin)
    button.pack(side = RIGHT, padx=1)

    rootA.mainloop()



def DelUser():
    os.remove(creds)
    rootA.destroy()
    # top.destroy()
    Signup()





def Path():

    def first():
        filepath = e.get()
        filewatch.LogWatcher(str(filepath)) # this passes the variable s to the function second() in the file twond.py

    top = Tk()

    L2 = Label(top, text="Enter the path of log file", font=("Helvetica"), height=4)
    L2.pack(side="left")


    directory = StringVar(None)
    e = Entry(top, textvariable=directory, width=50)
    e.pack(side="left")

    button4 = Button(top, text='click', command=first, bg="blue", fg="white")
    button4.pack(side=RIGHT, padx=1)
    button5 = Button(top, text='Quit', command=top.quit, font=("Helvetica", 10), fg='#a1dbcd', bg="#383a39")
    button5.pack(side=RIGHT, padx=1)
    top.mainloop()



def  WrongInput():
    top = Tk()
    Label(top, text="Invalid Username Or Password").grid(row=1,column=1)
    top.pack_slaves()
    top.mainloop()


if os.path.isfile(creds):
    Login()
else:
    Signup()

