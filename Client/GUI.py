
from tkinter import *
import cv2
import App
from threading import Timer
import time
from Detection import data
from Detection import running





def window():
     win = Tk()


     
     def register():
            data.name = var1.get()
            print(data.name)
            data.roll = var2.get()
            print(data.roll) 
            data.test_url = var3.get() 
            print(data.test_url)
            ent1.place_forget()
            ent3.place_forget()
            ent2.place_forget()
            btn1.place_forget()
            name1= Label(info,text=data.name)
            name1.place(x=120,y=10)
            roll1= Label(info,text=data.roll)
            roll1.place(x=120,y=40)
            test_url1= Label(info,text=data.test_url)
            test_url1.place(x=120,y=70)
            running.check_run()
            
            
 
      
     

     def func():
      
       a = StringVar
       a = 'Starting.....'
       label2 = Label(status,text =a)
       label2.place(x=4,y=4)
       App.App(win)
       
       

       
    

     
     win.minsize(width = 1400,height = 700)
     win.iconbitmap('Assets\Images\ICON2.ico')
     win.title("Proctifier")

     canvas2 = Canvas(win,bg='gray82',width=760,height=480)
     canvas2.place(x=640,y=0)

     canvas3 = Canvas(win,bg='gray82',width=1400,height=300)
     canvas3.place(x=0,y=480)

     status = Canvas(canvas3,bg='gray',width=1350,height=150)
     status.place(relx=.5, rely=.4,anchor= CENTER)

     label = Label(canvas3,text="Status:",)
     label.place(x=8,y=10)

     info = Canvas(canvas2,width= 700,height=200)
     info.place(relx=.5, rely=.27,anchor= CENTER)

     info2 = Canvas(canvas2,bg='white',width= 700,height=200)
     info2.place(relx=.5, rely=.73,anchor= CENTER)
     
     lbl1= Label(info,text='Name :')
     lbl1.place(x=10,y=10)
     var1=StringVar()
     ent1 = Entry(info,textvariable=var1)
     ent1.place(x=120,y=10)

     var2 = IntVar()
     lbl2= Label(info,text='Registration No.:')
     lbl2.place(x=10,y=40)
     ent2 = Entry(info,textvariable=var2)
     ent2.place(x=120,y=40)

     var3 = StringVar()
     lbl3= Label(info,text='Test URL:')
     lbl3.place(x=10,y=70)
     ent3 = Entry(info,textvariable=var3)
     ent3.place(x=120,y=70) 


     btn1 = Button(info,text='Register',command=register)
     btn1.place(x=4,y=100)

     btn = Button(info2,text="Start Procturing", command=func)
     btn.place(x=4,y=4)

     
     
    

     win.mainloop()
     