from tkinter import *
def redbg():
    text.config(bg="#fd0202", fg="#fff")
def bluebg():
    text.config(bg="#006699",fg="#fff")
def tealbg():
    text.config(bg="#008080",fg="#fff")
def helv():
    text.config(font=("Helvetica", 20))
def arial():
    text.config(font=("Arial", 20))
def monos():
    text.config(font=("Monospace", 20))
window = Tk()
text = Label(window, height=5, fg="#333", text="Hello, this will change when you click.")
text.grid(row=0,column=0)
btn1 = Button(window, height=2, width=10, text="Red", command=redbg)
btn1.grid(row=1,column=0)
btn2 = Button(window, height=2, width=10, text="Blue", command=bluebg)
btn2.grid(row=2,column=0)
btn3 = Button(window, height=2, width=10, text="Teal", command=tealbg)
btn3.grid(row=3,column=0)
btn11 = Button(window, height=2, width=10, text="Helvetica", command=helv)
btn11.grid(row=1,column=1)
btn21 = Button(window, height=2, width=10, text="Arial", command=arial)
btn21.grid(row=2,column=1)
btn31 = Button(window, height=2, width=10, text="Monospace", command=monos)
btn31.grid(row=3,column=1)
window.mainloop()
