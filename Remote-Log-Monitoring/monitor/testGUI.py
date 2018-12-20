from tkinter import *
import os
root= Tk()
root.title("My First GUI")
root.geometry("800x200")
frame1=Frame(root)
frame1.grid()

def helloCallBack():
     result = os.system('python Main.py')
     if result==0:
         print("OK")
         text1.insert(END,result)
     else:
         print("File Not Found")

label1 = Label(frame1, text = "Here is a label!")
label1.grid()

button1 = Button(frame1,text="Click Here" , foreground="blue",command= helloCallBack)
button1.grid()

text1 = Text(frame1, width = 35, height = 5,borderwidth=2)
text1.grid()


root.mainloop()