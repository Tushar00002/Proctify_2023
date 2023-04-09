import cv2
import numpy as np
from tkinter import *
from tkinter import ttk,messagebox
 
from PIL import Image, ImageTk 
import datetime
from Detection import data

def userImg() :
    cap = cv2.VideoCapture(0)

    def snapShot():
        cv2.rectangle(img1,(200,100),(450,350),(200,200,200),2)
        image = Image.fromarray(img1)
        time = str(datetime.datetime.now().today()).replace(":", " ")+ ".jpg"
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        # image.save(time)
        cv2.imwrite("ResultAssets/userFace/"+str(time), image)
        data.is_snap = True

        



    root = Tk()
    root.geometry("700x640")
    root.resizable(False,False)
    root.configure(bg="white")
    Label(root,text="Place your face inside the box and click OK", font=("times now roman", 20, "bold"), bg="white", fg= "black").pack(pady=10,padx=20)
   
    L1=Label(root,bg="red")
    L1.pack()
    # cap = cv2.VideoCapture(0)
    Button(root, text="OK", font=("times new roman",10,"bold"), bg="grey", fg="black", command=snapShot).pack(expand=True,pady=20)
    while True: 
        img = cap.read()[-1]
        if img is None:
            break
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cv2.rectangle(img1,(200,100),(450,350),(0,255,0),2)
        img = ImageTk.PhotoImage(Image.fromarray(img1))
        L1['image'] = img
        if(data.is_snap == True):
            print("done image")
            cap.release()
            root.destroy()
            break

        
        root.update() 



if __name__=="__main__":
    userImg()


