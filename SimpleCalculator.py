from tkinter import *
from tkinter import messagebox

Calculator=Tk()
Calculator.title("Calculator")

def append(text): #Adds the last pressed Character to the Input
    temp=var.get()
    temp+=text
    var.set(temp)

def clearFn(): #Clears the Input on pressing 'C'
    var.set("")

def delete(): #Clears the last Character in the Input on pressing 'Del'
    temp=var.get()
    temp=temp[:-1]
    var.set(temp)
    

def equals(event=None): #Gives the result of entered Input on pressing '='
    try:
        temp=var.get()
        temp2=str(eval(temp))
        var.set(temp2)
    except:
        messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=Calculator)
Calculator.bind('<Return>', equals) #Binds the 'Enter' key to function 'equals'

var=StringVar()

#This is the First Row 
displayBox=Entry(Calculator,textvariable=var,font=("Helvetica", 20),borderwidth=0,justify=RIGHT)
displayBox.grid(row=1,column=1,columnspan=6)

#This is the Second Row
btnSeven=Button(Calculator,text="7",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("7"))
btnSeven.grid(row=2,column=1)

btnEight=Button(Calculator,text="8",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("8"))
btnEight.grid(row=2,column=2)

btnNine=Button(Calculator,text="9",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("9"))
btnNine.grid(row=2,column=3)

btnDel=Button(Calculator,text="Del",width=4,font=("Helvetica", 14),borderwidth=0 ,command=delete)
btnDel.grid(row=2,column=4)

btnClear=Button(Calculator,text="C",width=4,font=("Helvetica", 14),borderwidth=0 ,command=clearFn)
btnClear.grid(row=2,column=5)

#This is the Third Row
btnFour=Button(Calculator,text="4",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("4"))
btnFour.grid(row=3,column=1)

btnFive=Button(Calculator,text="5",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('5'))
btnFive.grid(row=3,column=2)

btnSix=Button(Calculator,text="6",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('6'))
btnSix.grid(row=3,column=3)

btnAdd=Button(Calculator,text="+",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("+"))
btnAdd.grid(row=3,column=4)

btnDiv=Button(Calculator,text="/",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("/"))
btnDiv.grid(row=3,column=5)

#This is the Fourth Row
btnOne=Button(Calculator,text="1",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('1'))
btnOne.grid(row=4,column=1)

btnTwo=Button(Calculator,text="2",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('2'))
btnTwo.grid(row=4,column=2)

btnThree=Button(Calculator,text="3",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('3'))
btnThree.grid(row=4,column=3)

btnSub=Button(Calculator,text="-",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("-"))
btnSub.grid(row=4,column=4)

btnPer=Button(Calculator,text="%",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("%"))
btnPer.grid(row=4,column=5)

#This is the Fifth Row
btnZero=Button(Calculator,text="0",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('0'))
btnZero.grid(row=5,column=1)

btnZeroT=Button(Calculator,text="00",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('00'))
btnZeroT.grid(row=5,column=2)

btnPoint=Button(Calculator,text=".",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append('.'))
btnPoint.grid(row=5,column=3)

btnMul=Button(Calculator,text="*",width=4,font=("Helvetica", 14),borderwidth=0 ,command=lambda:append("*"))
btnMul.grid(row=5,column=4)

btnAns=Button(Calculator,text="=",width=4,font=("Helvetica", 14),borderwidth=0 ,command=equals)
btnAns.grid(row=5,column=5)

Calculator.mainloop()
