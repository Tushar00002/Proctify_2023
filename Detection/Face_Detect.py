import cv2
from Detection import data
import time


def face_dec(frame):
        
        if(data.check == False):
                data.start =  time.mktime(time.localtime())
        data.end =  time.mktime(time.localtime())
        face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        col = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cap.detectMultiScale(
                 col,
                 scaleFactor = 1.1,
                 minNeighbors = 5,
                 minSize = (30,30),
                 flags = cv2.CASCADE_SCALE_IMAGE
            )
        count=0
        
        for(x,y,w,h) in faces:
                 count = count + 1
                 cv2.rectangle(frame,(x,y),(x+w,x+h),(0,255,0),2)
                 if count>=2:
                         data.check = True
                         data.end =  time.mktime(time.localtime())
                         #print(data.end-data.start)
                         
                         data.multiple_count = data.multiple_count + 1
                         data.ismulti = True
                         if(data.end - data.start >=4):
                           print('Multiple face for 4 sec')
                           data.multi4 = data.multi4 + 1
                         print("Multiple Face Detected from Harcascade")
                         if(data.img_mul<=3):
                          data.mul_img[data.img_mul] ='ResultAssets/Multiple_Face/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
                          cv2.imwrite( 'ResultAssets/Multiple_Face/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                          data.img_mul = data.img_mul + 1
                 if(count == 1):
                        data.check = False      
                         
                         
                         
                 