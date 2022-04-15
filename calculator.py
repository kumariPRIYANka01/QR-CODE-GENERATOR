from tkinter import *
import parser 

root=Tk()
root.title('Calculator')


#adding the input field
i=0
def getvariables(num):
    global i
    display.insert(i,num)
    i+=1

def clearall():
    display.delete(0,END)

def undo():
    entirestring=display.get()
    if len(entirestring):
        newstring=entirestring[:-1]
        clearall()
        display.insert(0,newstring)
    else:
        clearall()
        display.insert(0,"error")

def calculate():
    entirestring=display.get()
    try:
        a=parser.expr(entirestring).compile()
        result=eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,"error")

def getoperator(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length
#adding the input field
display= Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#button for calculator
Button(root, text="1",command=lambda:getvariables(1)).grid(row=2,column=0)
Button(root, text="2",command=lambda:getvariables(2)).grid(row=2,column=1)
Button(root, text="3",command=lambda:getvariables(3)).grid(row=2,column=2)

Button(root, text="4",command=lambda:getvariables(4)).grid(row=3,column=0)
Button(root, text="5",command=lambda:getvariables(5)).grid(row=3,column=1)
Button(root, text="6",command=lambda:getvariables(6)).grid(row=3,column=2)

Button(root, text="7",command=lambda:getvariables(7)).grid(row=4,column=0)
Button(root, text="8",command=lambda:getvariables(8)).grid(row=4,column=1)
Button(root, text="9",command=lambda:getvariables(9)).grid(row=4,column=2)

#adding other buttons to calc
Button(root,text="0",command=lambda:getvariables(0)).grid(row=5,column=0)
Button(root,text="AC",command=lambda:clearall()).grid(row=5,column=1)
Button(root,text="=",command=lambda:calculate()).grid(row=5,column=6)

Button(root,text="+",command=lambda:getoperator("+")).grid(row=2,column=4)
Button(root,text="-",command=lambda:getoperator("-")).grid(row=3,column=4)
Button(root,text="x",command=lambda:getvariables("*")).grid(row=4,column=4)
Button(root,text="/",command=lambda:getvariables("/")).grid(row=5,column=4)
Button(root,text="del",command=lambda:undo()).grid(row=2,column=5)
Button(root,text="x!",command=lambda:getvariables("(x-1)")).grid(row=3,column=5)
Button(root,text="exp",command=lambda:getvariables("**")).grid(row=4,column=5)
Button(root,text=")",command=lambda:getvariables(")")).grid(row=5,column=5)
Button(root,text="(",command=lambda:getvariables("(")).grid(row=5,column=2)


root.mainloop()