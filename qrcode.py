from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()

def command1():
    link_name=nameentry.get()
    link=linkentry.get()
    file_name=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)

canvas=Canvas(root,width=400,height=500)
canvas.pack()


app_label=Label(root,text="QR Code Generator",fg="blue",font=("Arial", 30))
canvas.create_window(200,50,window=app_label)


namelabel=Label(root,text="link name")
link=Label(root,text="link")
canvas.create_window(200,100,window=namelabel)
canvas.create_window(200,160,window=link)

nameentry=Entry(root)
linkentry=Entry(root)
canvas.create_window(200,130,window=nameentry)
canvas.create_window(200,180,window=linkentry)


button=Button(text="generate QR code",command=command1)
canvas.create_window(200,230,window=button)

root.mainloop()
