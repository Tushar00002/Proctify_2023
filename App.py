import tkinter
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import time
from Detection import Face_Detect
from Detection import head_pose
from Detection import Multiple_Face
from Detection import win_switch
from Object import Object_Detector


face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


 
class App:
     def __init__(self, window,video_source=0):
         self.window = window
         
         self.video_source = video_source
 
         
         self.vid = MyVideoCapture(self.video_source)
         

 
         
         self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
         self.canvas.place(x=340,y=90)
         
         
         
 
        
         self.delay = 2
         self.update()
 
         
 
     def snapshot(self):
         ret, frame = self.vid.get_frame()
 
         if ret:
             cv2.imwrite( 'frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
     def update(self):
     
         ret, frame = self.vid.get_frame()
         
         head_pose.face_dir(frame)
         Multiple_Face.face2(frame)
         Object_Detector.object(frame)
         Face_Detect.face_dec(frame)
         win_switch.test()
         
            
        
         
         
         

        
         

         

         if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
         self.window.after(self.delay, self.update)

 
class MyVideoCapture:
     def __init__(self, video_source=0):
        
         self.vid = cv2.VideoCapture(video_source)
         
 
         
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
 
     def get_frame(self):
         if self.vid.isOpened():
             ret, frame = self.vid.read()
         
             if ret:
                 
                 
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             
             else:
                 return (ret, None)
         else:
             return (ret, None)
 
     
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
 

