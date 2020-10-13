from tkinter import *

def backspace():
     #adding a try block so that user can not tamper with result
    try: 
        if tbox.get()[0]=="=":clear()
    except IndexError: 
        pass
    prev = tbox.get()
    clear()
    tbox.insert(0,prev[:-1])

def clear():
    tbox.delete(0, END)

def key_pressed(key):
    #adding a try block so that user can not tamper with result
    try:
        if tbox.get()[0]=="=": clear() 
    except IndexError:
        pass

    #adding a try block when user has already inputted a operator
    try:
        if tbox.get()[-1] in "+-*/" and str(key) in "+-*/":
            tbox.delete(len(tbox.get())-1)  
    except IndexError:
        pass    
    tbox.insert(END, str(key))

def equal():
    try:
        if tbox.get()[0] in "*/": tbox.delete(0)
    except IndexError:
        pass

    try: 
        if tbox.get()[-1] in "+-*/": tbox.delete(len(tbox.get())-1) 
    except IndexError:
        pass       

    answer = eval(tbox.get())
    clear()
    tbox.insert(0,"="+str(answer))

root = Tk()
root.geometry('348x450')

Label(text="Calculator", font=('Arial',20), fg="grey", bg='purple').place(x=100,y=30)

tbox = Entry(font=('Arial',20))
tbox.place(x=0, y=110)

#1st row
#Button(text="", width=10, height=2).place(x=0,y=180)
Button(text="C", command=clear, width=22, height=2).place(x=0,y=180)
Button(text="<--", command=backspace, width=10, height=2).place(x=176,y=180)
Button(text="/", command=lambda:key_pressed('/'), width=10, height=2).place(x=262.5,y=180)

#2nd row
Button(text=7, command=lambda:key_pressed(7), width=10, height=2).place(x=0,y=234)
Button(text=8, command=lambda:key_pressed(8), width=10, height=2).place(x=87.5,y=234)
Button(text=9, command=lambda:key_pressed(9), width=10, height=2).place(x=175,y=234)
Button(text='*', command=lambda:key_pressed('*'), width=10, height=2).place(x=262.5,y=234)

#3rd row
Button(text=4, command=lambda:key_pressed(4), width=10, height=2).place(x=0,y=288)
Button(text=5, command=lambda:key_pressed(5), width=10, height=2).place(x=87.5,y=288)
Button(text=6, command=lambda:key_pressed(6), width=10, height=2).place(x=175,y=288)
Button(text='-', command=lambda:key_pressed('-'), width=10, height=2).place(x=262.5,y=288)

#4th row
Button(text=1, command=lambda:key_pressed(1), width=10, height=2).place(x=0,y=342)
Button(text=2, command=lambda:key_pressed(2), width=10, height=2).place(x=87.5,y=342)
Button(text=3, command=lambda:key_pressed(3), width=10, height=2).place(x=175,y=342)
Button(text='+', command=lambda:key_pressed('+'), width=10, height=2).place(x=262.5,y=342)

#5th row
Button(text=0, command=lambda:key_pressed(0), width=32, height=2).place(x=0,y=396)
Button(text='=', command=equal, width=10, height=2).place(x=262.5,y=396)

root.mainloop()
