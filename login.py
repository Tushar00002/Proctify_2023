from tkinter import *
from tkinter import messagebox
# import ast
import pymysql
import Configure
# import GUI as gui


########################################### BASIC LAYOUT ##############################################

def gui():
    root=Tk()
    root.title('Login')
    root.geometry('975x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)
    root.iconbitmap('Assets\Images\ICON2.ico')

    ########################################### FUNCTIONS ##########################################

    def forgot():
        root.destroy()


    def clear():
        user.delete(0,END)
        code.delete(0,END)
        
        
    ############--------------------- SIGN IN FUNCTIONS -----------------################

    def signin():
        username=user.get()
        password=code.get()

        if username==' ' or password==' ':
            messagebox.showerror('Error','All Fields Are Required')

        else:
            try:
                con=pymysql.connect(host='localhost',
                                        user='root',
                                        password='Tushar@280702')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Connection is not estabilished try again')
                return


            query='use userdata2'
            mycursor.execute(query)
            query=('select*from data where username=%s and password=%s')
            mycursor.execute(query,(username,password))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username or pasword')
            else:
                messagebox.showinfo('Welcome','Login is successful')
                
                clear()
                root.destroy()
                Configure.userImg()
                print("reached here")
                import main
                print("reached here again")
                
 
    def signup_command():
        root.destroy()
        import sign_up


    ############################################### UI ###############################################
        

    img=PhotoImage(file='Assets\Images\lg.png')
    Label(root,image=img,bg='white').place(x=5,y=10)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=170,y=5) 

    ######################################### USER NAME ################################################
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):   
        name=user.get()
        if name=='':
         user.insert(0,'Username') 

    user = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=120,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=395,height=2,bg='black').place(x=118,y=107)

    ####################################### PASSWORD ######################################################
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):   
        name=code.get()
        if name=='':
         code.insert(0,'Password') 

    code = Entry(frame,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=120,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=395,height=2,bg='black').place(x=118,y=177)

    ################################################# BUTTONS ##########################################################

    Button(frame,width=33,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command = signin).place(x=120,y=224)
    label=Label(frame,text="Don't have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=120,y=280)

    sign_up= Button(frame,width=6,text='Sign up',border=0,cursor='hand2',bg='white',fg='#57a1f8',command = signup_command)
    sign_up.place(x=260,y=280)

    # label=Label(frame,text="Forgot Password?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    # label.place(x=120,y=250)

    forgot= Button(frame,width=15,text='Forgot Password?',border=0,cursor='hand2',bg='white',fg='#57a1f8',command = forgot)
    forgot.place(x=240,y=190)

    

    root.mainloop() # END

gui()

