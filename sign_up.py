from tkinter import *
from tkinter import messagebox
#import GUI as gui
# import ast
import pymysql
# import login as log

################################################ LAYOUT ##############################################

window=Tk()
window.title("SignUp")
window.geometry('975x500+300+120')
window.configure(bg="#fff")
window.resizable(False,False)

# def hide():
#     openeye.config(file='openeye.png')
#     password.config(show='*')
#     eyebutton.config(command=show)

# def show():
#     openeye.config(file='closeeye.png')
#     password.config(show ='')
#     eyebutton.CONFIG(command=hide)

################################################ FUNCTIONS ############################################################

def clear():
    email.delete(0,END)
    user.delete(0,END)
    code.delete(0,END)
    confirm_code.delete(0,END)
    

def signup():
    mail=email.get()
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    
    
    
################################################# DATABASE WORK #########################################################

    if password==confirm_password:

        try:

            con=pymysql.connect(host='localhost',
                                user='root',
                                password='Tushar@280702')
            
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue , Please Try Again')
            return

        try:
            

            query= 'create database userdata2'
            mycursor.execute(query)
            query='use userdata2'
            mycursor.execute(query)
            query="CREATE TABLE data(S_No integer auto_increment primary key not null,Email varchar(50),Username varchar(30),Password varchar(20))"
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata2')

        
##################------------------- FILLING DATA ---------------------######################


        # checking for same username 
        
        query=('select*from data where username=%s')
        mycursor.execute(query,(username))
        row=mycursor.fetchone()   #search username in database
        if row != None:
            messagebox.showerror('Error','Username Already exists')

        else: #insert data

            query='insert into data(Email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(mail,username,password))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            window.destroy()
            import login

#######################################---------------------------------------



        # try:
        #     file=open('datasheet.txt','r+')
        #     d=file.read()
        #     r=ast.literal_eval(d)

        #     dict2={username:password}
        #     r.update(dict2)
        #     file.truncate(0)
        #     file.close()
        #     if username in r.keys():
        #         messagebox.showinfo('Failed','username taken')
        #     else:

        #         file=open('datasheet.txt','w')
        #         w=file.write(str(r))

        #         messagebox.showinfo('signup', 'Successfully sign up')

        # except:
        #         file=open('datasheet.txt','w')
        #         pp=str({'Username':'password'})
        #         file.write(pp)
        #         file.close()

    else:
        messagebox.showerror('Invalid', "Both Password should match")

#########################################--------------------------------------------

def sign():
    window.destroy()
    import login
    # login.window()   
    
######################### IMAGE AND SIGN IN LAYOUT ######################

img=PhotoImage(file='Assets\Images\lg.png')
Label(window,image=img,bg='white').place(x=5,y=5)

frame=Frame(window,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=170,y=0) 
#####################-------------------------- EMAIL ---------------------######################## 

def on_enter(e):
    email.delete(0,'end')

def on_leave(e):   
    name=email.get()
    if name=='':
       email.insert(0,'Email') 

email = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
email.place(x=120,y=80)
email.insert(0,'Email')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)

Frame(frame,width=395,height=2,bg='black').place(x=118,y=107)




######################------------------------ USERNAME ----------------------------#############################

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):   
    name=user.get()
    if name=='':
       user.insert(0,'Username') 

user = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=120,y=140)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=395,height=2,bg='black').place(x=118,y=167)
#######################----------------------------PASSWORD---------------------------#######################
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):   
    name=code.get()
    if name=='':
       code.insert(0,'Password') 

code = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=120,y=193)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=395,height=2,bg='black').place(x=118,y=220)

######################-------------------------------COMFIRM PASSWORD-------------------------##########################

def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):   
    name=confirm_code.get()
    if name=='':
       confirm_code.insert(0,'Password') 

confirm_code = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
confirm_code.place(x=120,y=250)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame,width=395,height=2,bg='black').place(x=118,y=277)

########################------------------------------------------
# openeye=PhotoImage(file='openeye.png')
# eyebutton=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2')
# eyebutton.place(x=320,y=195)



############################################### BUTTONS ##############################################


Button(frame,width=35,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=118,y=290)
label=Label(frame,text="I have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=120,y=330)

signin= Button(frame,width=6,text='Sign in',border=0,cursor='hand2',bg='white',fg='#57a1f8',command=sign)
signin.place(x=230,y=330)





window.mainloop()