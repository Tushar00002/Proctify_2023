from tkinter import *
import time
import ttkthemes
from tkinter import ttk
import ast
import pymysql
import App
import result
from Detection import data
from Detection import running
import Configure
from tkinter import messagebox

############################### CREATE DATABASE ################################




####################### Functions ############################

def gui_main():

    def p_stop():
        gui.destroy()

    def proctor():
         if(data.isregister == True):
             rightFrame=Frame(gui)
            #  rightFrame.place(x=330,y=160,width=920,height=600)
             running.check_run()
             data.is_proctor == True
             proctoringButton.place_forget()
             stop = ttk.Button(leftFrame,text = "Stop Proctoring",command=p_stop)
             stop.place(x=40,y=500)
             
             App.App(gui)
         else:
             messagebox.askokcancel(title="Warning",message="Please Register to start Proctoring")


    def clock():
        global date,currenttime
        date= time.strftime('%d/%m/%Y')
        currenttime=time.strftime('%H:%M:%S')
        datetimeLable.after(1000,clock)



    def Details():

        

        def connect():
            
            print(nameEntry.get(),rollEntry.get(),branchEntry.get(),classEntry.get())
            detailsButton
            global roll,name,branch,clas
            roll=rollEntry.get()
            name=nameEntry.get()
            data.name = name
            data.roll  = roll
            branch=branchEntry.get()
            clas=classEntry.get()
            global mycursor,con
            if name=='' or roll=='' or branch=='' or clas=='' :
                messagebox.showerror('Error','All fields are required')

            else:
                data.isregister = True
                
                try:

                    con=pymysql.connect(host='localhost',
                                        user='root',
                                        password='Tushar@280702')
                    
                    mycursor=con.cursor()
                except:
                    messagebox.showerror('Error','Database Connectivity Issue , Please Try Again')
                    return

                try:
                    

                    query= 'create database pc'
                    mycursor.execute(query)
                    query='use pc'
                    mycursor.execute(query)
                    query="CREATE TABLE data(S_No integer auto_increment primary key not null,name varchar(20),rollno varchar(30),branch varchar(20),class varchar(20))"
                    mycursor.execute(query)

                except:
                    mycursor.execute('use pc')

                query='insert into data(name,rollno,branch,class) values(%s,%s,%s,%s)'
                mycursor.execute(query,(name,roll,branch,clas))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details are filled')
                detailsWindow.destroy()

                nameLabel_display=Label(leftFrame,
                                        text='Name  : ', 
                                        font=('Microsoft YaHei UI Light',11))
                nameLabel_display.place(x=10,y=250)
                nameEntry_display=Label(leftFrame,
                                        text=name,
                                        font=('Microsoft YaHei UI Light',11))
                nameEntry_display.place(x=70,y=250)

                rollLabel_display=Label(leftFrame,
                                        text='Roll No.: ', 
                                        font=('Microsoft YaHei UI Light',11))
                rollLabel_display.place(x=10,y=280)
                rollEntry_display=Label(leftFrame,
                                        text=roll,
                                        font=('Microsoft YaHei UI Light',11))
                rollEntry_display.place(x=70,y=280)

                branchLabel_display=Label(leftFrame,
                                        text='Branch : ', 
                                        font=('Microsoft YaHei UI Light',11))
                branchLabel_display.place(x=10,y=310)
                branchEntry_display=Label(leftFrame,
                                        text=branch,
                                        font=('Microsoft YaHei UI Light',11))
                branchEntry_display.place(x=70,y=310)

                classLabel_display=Label(leftFrame,
                                        text='Class : ', 
                                        font=('Microsoft YaHei UI Light',11))
                classLabel_display.place(x=10,y=340)
                classEntry_display=Label(leftFrame,
                                        text=clas,
                                        font=('Microsoft YaHei UI Light',11))
                classEntry_display.place(x=70,y=340)
                
                
                date_display=Label(leftFrame,
                                    text='Date  : ', 
                                    font=('Microsoft YaHei UI Light',11))
                date_display.place(x=10,y=370)
                date_display=Label(leftFrame,
                                    text=date,
                                    font=('Microsoft YaHei UI Light',11))
                date_display.place(x=70,y=370)
                
                
                time_display=Label(leftFrame,
                                    text='Time : ', 
                                    font=('Microsoft YaHei UI Light',11))
                time_display.place(x=10,y=400)
                time_display=Label(leftFrame,
                                    text=currenttime,
                                    font=('Microsoft YaHei UI Light',11))
                time_display.place(x=70,y=400)

                
                
    #############################################################################################################################################################################
            
        detailsWindow=Toplevel()
        detailsWindow.geometry('400x300+250+150')
        detailsWindow.title('Your Details') 
        detailsWindow.resizable(False,False)

        global nameEntry,rollEntry,branchEntry,classEntry

        nameLabel=Label(detailsWindow,
                        text='Name :', 
                        font=('Microsoft YaHei UI Light',11))
        nameLabel.grid(row=0,column=0,padx=20,sticky=W)

        nameEntry=Entry(detailsWindow,
                        font=('Microsoft YaHei UI Light',11))
        nameEntry.grid(row=0,column=1,padx=10,pady=20)

        rollLabel=Label(detailsWindow,
                        text='Roll No. :', 
                        font=('Microsoft YaHei UI Light',11))
        rollLabel.grid(row=1,column=0,padx=20,sticky=W)

        rollEntry=Entry(detailsWindow,
                        
                        font=('Microsoft YaHei UI Light',11))
                        
        rollEntry.grid(row=1,column=1,padx=10,pady=20)               

        branchLabel=Label(detailsWindow,
                        text='Branch :', 
                        font=('Microsoft YaHei UI Light',11))
        branchLabel.grid(row=2,column=0,padx=20,sticky=W)

        branchEntry=Entry(detailsWindow,
                        
                        font=('Microsoft YaHei UI Light',11))
        text_label.place_forget()
                        
        branchEntry.grid(row=2,column=1,padx=10,pady=20)
        
        classLabel=Label(detailsWindow,
                        text='Class :', 
                        font=('Microsoft YaHei UI Light',11))
        classLabel.grid(row=3,column=0,padx=20,sticky=W)

        classEntry=Entry(detailsWindow,
                        
                        font=('Microsoft YaHei UI Light',11))
                        
        classEntry.grid(row=3,column=1,padx=10,pady=20)
        print(nameEntry.get(),rollEntry.get(),branchEntry.get(),classEntry.get())
        doneButton= ttk.Button(detailsWindow,text='Done :',command=connect).grid(row=4,column=1,padx=0)


    ###############################  GUI  ###########################################################################################################

    gui = ttkthemes.ThemedTk()

    gui.get_themes()
    gui.iconbitmap('Assets\Images\ICON2.ico')
    gui.set_theme('radiance')
    gui.configure(bg='gray82')

    gui.geometry('1080x700+130+70') 
    gui.title('Proctoring System') 
    gui.resizable(False,False)

    datetimeLable=Label(gui,font =('Microsoft YaHei UI Light',11))
    datetimeLable.place(x=5,y=5)
    clock()

    mainLabel = Label(gui,text='Proctify', font=('Microsoft YaHei UI Light',20,'bold'), width =  30,bg='gray82')
    mainLabel.place(x=400 ,y=10)

    leftFrame=Frame(gui)
    leftFrame.place(x=20,y=80,width=230,height=600)

    logo_image=PhotoImage(file='Assets\Images\eacher.png',master=gui)
    logo_Label=Label(leftFrame,image=logo_image).place(x=65,y=10) 
    # logo_Label.grid(row=0,column=1)
    text_label= Label(leftFrame,text="Enter your details :",font=('Microsoft YaHei UI Light',10))
    text_label.place(x=45,y=100)
    rightFrame=Frame(gui)
    rightFrame.place(x=330,y=80,width=666,height=500)

    text1='Start Proctoring'

    proctoringButton= ttk.Button(leftFrame,text = text1,command=proctor)
    proctoringButton.place(x=40,y=500) 

    detailsButton= ttk.Button(gui,text='Details :',command=Details).place(x=60,y=220)

    

        



    # connectDatabaseButton= ttk.Button(gui,text='Connect Database :',command=connectDatabase).place(x=25,y=180) 





    gui.mainloop() 
    print("Executed")
    result.res()


gui_main()