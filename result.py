from tkinter import *
from Detection import data
import pdf_generator
from PIL import ImageTk, Image
import tkinter.font as tkFont

def res():
 win = Tk()
 
 win.minsize(width=800, height=500)
 canvas2 = Canvas(win,bg='gray82',width=750,height=100)
 canvas2.place(x=25,y=25)
 var ='Name :'
 lbl1 = Label(canvas2,text = var)
 lbl1.place(x=10,y=10)
 lbl2 = Label(canvas2,text = data.name)
 lbl2.place(x=50,y=10)

 lbl1 = Label(canvas2,text = 'Roll No.:')
 lbl1.place(x=10,y=40)
 lbl2 = Label(canvas2,text = data.roll)
 lbl2.place(x=80,y=40)

 canvas2 = Canvas(win,bg='gray82',width=750,height=350,)
 canvas2.place(x=25,y=125)
 

 fontObj = tkFont.Font(size=48)
 lbl = Label(canvas2,text="Test Submitted",font=fontObj,bg='gray60',fg="gray82",justify='center')
 lbl.place(x=110,y=130)

 pdf_generator.pdf_gen()
 print(data.URL)
 print(data.softwares)

 print(data.res.keys())





 win.after(1500,lambda:win.destroy())
 win.mainloop()

# res()