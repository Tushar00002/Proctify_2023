from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import login

win = Tk()
win.title("Third Eye") #-> to put title on gui


# to put icon we need ico file
win.iconbitmap('Assets\Images\ICON2.ico')

# Window_Size

win.minsize(width = 1520,height = 800)


img = ImageTk.PhotoImage(Image.open("Assets\Images\yac.jpg")) 

canvas1 = Canvas( win, width = 900,height = 500)
  
canvas1.pack(fill = "both", expand = True)

fontObj = tkFont.Font(size=48)
lbl = Label(canvas1,text="Proctify",font=fontObj,bg='#000000',fg="#ffffff")
lbl.place(x=360,y=30)

bt1 = Button(canvas1,text = 'Login')
bt1.place(x=100,y=200)
  
canvas1.create_image( 0, 0, image = img,anchor = "nw")

info = Label()
win.after(1500,lambda:win.destroy())
win.mainloop()

login.gui()