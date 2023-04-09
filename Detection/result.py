from tkinter import *
import data

win = Tk()

win.minsize(width =1200,height = 600)

canvas2 = Canvas(win,bg='gray82',width=500,height=100)
canvas2.place(x=20,y=20)

lbl1 = Label(canvas2,text = 'Name:')
lbl1.place(x=10,y=10)
lbl2 = Label(canvas2,text = data.name)
lbl2.place(x=80,y=10)

lbl1 = Label(canvas2,text = 'Roll No.:')
lbl1.place(x=10,y=40)
lbl2 = Label(canvas2,text = data.roll)
lbl2.place(x=80,y=40)

canvas3 =Canvas(win,bg='gray82',width=1160,height=440)
canvas3.place(x=20,y=140)


canvas11 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas11.place(x=210,y=20)

canvas12 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas12.place(x=400,y=20)

canvas13 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas13.place(x=590,y=20)

canvas14 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas14.place(x=780,y=20)

canvas15 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas15.place(x=970,y=20)

canvas16 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas16.place(x=20,y=20)


if(data.multi4 != 0):
    lbl1 = Label(canvas11,text = 'Multiple Face Detected')
    lbl1.place(x=10,y=10)

if(data.Left != 0):
    lbl2 = Label(canvas12,text = 'Suspicious Head Movement -> Left')
    lbl2.place(x=10,y=10)

if(data.Right != 0):
    lbl3 = Label(canvas13,text = 'Suspicious Head Movement -> Right')
    lbl3.place(x=10,y=10)

if(data.Down != 0):
    lbl4 = Label(canvas14,text = 'Suspicious Head Movement -> Down')
    lbl4.place(x=10,y=10)







win.mainloop()


     

 