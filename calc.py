from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.title('Calculator')
root.geometry('350x450')

def backspace():
    lbl_data.set(lbl_data.get()[0:-1])

def clear():
    lbl_data.set('')

def result():
    try:
        lbl_data.set(eval(lbl_data.get()))
    except: 
        messagebox.showerror('Calculator', 'Invalid Input')    
                
def btn_clicked (btn):
    lbl_data.set(lbl_data.get()+btn['text'])

lbl_data = StringVar()
lbl = Label(
    root,
    anchor = SE,
    font = ("Verdana", 35),
    background = "#ffffff",
    fg = "#000000",
    textvariable = lbl_data
)
lbl.pack(expand = True, fill = "both")

btn_pack0 = Frame(root)
btn_pack0.pack(expand=True, fill=BOTH)

btn_pack1 = Frame(root)
btn_pack1.pack(expand=True, fill=BOTH)

btn_pack2 = Frame(root)
btn_pack2.pack(expand=True, fill=BOTH)

btn_pack3 = Frame(root)
btn_pack3.pack(expand=True, fill=BOTH)

btn_pack4 = Frame(root)
btn_pack4.pack(expand=True, fill=BOTH)
#----------------------------------------------------------------------------------

Button(btn_pack0,
    text="%",
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    state=DISABLED
).pack(side=LEFT,expand=True, fill=BOTH)


Button(
    btn_pack0,
    text='C',
    bg='#F1948A',
    font=('Consolas', 22),
    border=0,
    command=clear,
).pack(side=LEFT, expand=True, fill=BOTH)

Button(
    btn_pack0,
    text='<',
    bg='#F1948A',
    font=('Consolas', 22),
    border=0,
    command=backspace,
).pack(side=LEFT, expand=True, fill=BOTH)

division = Button(
        btn_pack0,
        text='/',
        font=('Consolas', 22),
        bg='#fdefe9',
        border=0,
        command=lambda: btn_clicked(division),
)
division.pack(side=LEFT, expand=True, fill=BOTH)

#-----------------------------------------------------------------------------------------
bt1 = Button(btn_pack1,
    text = '1',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt1)
)
bt1.pack(side=LEFT,expand=True, fill=BOTH)
 
bt2 = Button(btn_pack1,
    text = '2',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt2)
)
bt2.pack(side=LEFT,expand=True, fill=BOTH)

bt3 = Button(btn_pack1,
    text = '3',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt3)
)
bt3.pack(side=LEFT,expand=True, fill=BOTH)

multiplication = Button(btn_pack1,
        text='*',
        font=('Consolas', 22),
        bg='#fdefe9',
        border=0,
        command=lambda: btn_clicked(multiplication)
   
)
multiplication.pack(side=LEFT, expand=True, fill=BOTH)

#------------------------------------------------------------------------------------

bt4 = Button(btn_pack2,
    text='4',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt4)
)
bt4.pack(side=LEFT,expand=True, fill=BOTH)

bt5 = Button(btn_pack2,
    text='5',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt5)
)
bt5.pack(side=LEFT,expand=True, fill=BOTH)

bt6 = Button(btn_pack2,
    text='6',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt6)
)
bt6.pack(side=LEFT,expand=True, fill=BOTH)

addition = Button(btn_pack2,
        text='+',
        font=('Consolas', 22),
        bg='#fdefe9',
        border=0,
        command=lambda: btn_clicked(addition)
   )
addition.pack(side=LEFT, expand=True, fill=BOTH)

#-----------------------------------------------------------------------------------

bt7 = Button(btn_pack3,
    text='7',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt7)
)
bt7.pack(side=LEFT,expand=True, fill=BOTH)

bt8 = Button(btn_pack3,
    text='8',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt8)
)
bt8.pack(side=LEFT,expand=True, fill=BOTH)

bt9 = Button(btn_pack3,
    text='9',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt9)
)
bt9.pack(side=LEFT,expand=True, fill=BOTH)

subtraction = Button(btn_pack3,
        text='-',
        font=('Consolas', 22),
        bg='#fdefe9',
        border=0,
        command=lambda: btn_clicked(subtraction)
   )
subtraction.pack(side=LEFT, expand=True, fill=BOTH)

#--------------------------------------------------------------------------------------

Button(btn_pack4,
    text=" ",
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    state=DISABLED
).pack(side=LEFT,expand=True, fill=BOTH)

bt0 = Button(btn_pack4,
    text='0',
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    command= lambda: btn_clicked (bt0)
)
bt0.pack(side=LEFT,expand=True, fill=BOTH)

Button(btn_pack4,
    text=" ",
    font=('Consolas', 22),
    border=0,
    relief=GROOVE,
    bg='#CACFD2',
    state=DISABLED
).pack(side=LEFT,expand=True, fill=BOTH)

equal = Button(btn_pack4,
        text='=',
        font=('Consolas', 22),
        bg='#a6e7ff',
        border=0,
        command=result
   )
equal.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()