from tkinter import *
import math
def sum():
    int1 = int(E1.get())
    int2 = int(E2.get())
    ans.config(text=int1+int2)
def dif():
    int1 = int(E1.get())
    int2 = int(E2.get())
    ans.config(text=int1-int2)
def mul():
    int1 = int(E1.get())
    int2 = int(E2.get())
    ans.config(text=int1*int2)
def div():
    int1 = int(E1.get())
    int2 = int(E2.get())
    ans.config(text=int1/int2)
def raised():
    int1 = int(E1.get())
    int2 = int(E2.get())
    ans.config(text=int1**int2)
def root():
    int1 = int(E3.get())
    ans2.config(text=math.sqrt(int1))
window = Tk()
E1 = Entry(window, width=10)
E1.grid(row=0,column=0)
E2 = Entry(window, width=10)
E2.grid(row=0,column=1)
plus = Button(window, text="+",bg="#006699",fg="#fff",relief=FLAT,command=sum,width=5)
minus = Button(window, text="-",bg="#006699",fg="#fff",relief=FLAT, command=dif,width=5)
multiply = Button(window, text="x",bg="#006699",fg="#fff",relief=FLAT, command=mul,width=5)
divide = Button(window, text="/",bg="#006699",fg="#fff",relief=FLAT, command=div,width=5)
raised = Button(window, text="^",bg="#006699",fg="#fff",relief=FLAT, command=raised,width=5)
plus.grid(row=1,column=0)
minus.grid(row=1,column=1)
multiply.grid(row=2,column=0)
divide.grid(row=2,column=1)
raised.grid(row=3,column=0)
text = Label(window, text="Answer: ")
text.grid(row=4,column=0)
ans = Label(window, text="")
ans.grid(row=4,column=1)
#stuff
separate = Label(window, text="Other functions:")
separate.grid(row=5,column=0)
E3 = Entry(window, width=10)
E3.grid(row=6,column=0)
root = Button(window, text="Square root",bg="#006699",fg="#fff",relief=FLAT, command=root,width=10)
root.grid(row=7,column=0)
#sin = Button(window, text="Sin",bg="#006699",fg="#fff",relief=FLAT, command=sin,width=10)
#sin.grid(row=7,column=1)
ans2 = Label(window, text="")
ans2.grid(row=8,column=0)
window.mainloop()
