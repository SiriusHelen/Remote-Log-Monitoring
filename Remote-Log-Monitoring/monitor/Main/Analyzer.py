
import Result
from tkinter import *



def Path():

    def first():
        url = e.get()
        Result.URL_results(str(url)) # this passes the variable s to the function second() in the file twond.py

    top = Tk()

    L2 = Label(top, text="Enter Url Here", font=("Helvetica"), height=4)
    L2.pack(side="left")


    directory = StringVar(None)
    e = Entry(top, textvariable=directory, width=50)
    e.pack(side="left")


    button5 = Button(top, text='Quit', command=top.quit, font=("Helvetica", 10), fg='red', bg="white")
    button5.pack(side=RIGHT, padx=1)
    button4 = Button(top, text='Analyze', command=first, bg="white", fg="black")
    button4.pack(side=RIGHT, padx=1)

    top.mainloop()





def main():
    Path()


if __name__ == '__main__':
    main()
