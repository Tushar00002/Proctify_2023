import cv2
import mediapipe as mp
import time
from Detection import data
import App

faceDetector = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils


def face2(frame):
 if(data.check_miss == False):
   data.start_miss = time.mktime(time.localtime())

 data.end_miss = time.mktime(time.localtime())  

 with faceDetector.FaceDetection(

    min_detection_confidence=0.5) as face_detection:

    count = 0
    event = 0

    start = time.time()

    
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
 
    if results.detections:
      for id, detection in enumerate(results.detections):
        drawing.draw_detection(image, detection)
        count = count + 1
       

   

    if(count==0):
      data.check_miss = True
      print("User missing")
      if(data.end_miss - data.start_miss >= 3):
          data.usermiss = data.usermiss + 1
          if(data.pic_taken<=3):
           data.img[data.pic_taken] = 'ResultAssets/User_Miss/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
           cv2.imwrite( 'ResultAssets/User_Miss/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
           data.pic_taken = data.pic_taken + 1
          print(data.usermiss)
          data.check_miss = False
      

    end = time.time()
    totalTime = end - start

    fps = 1 / totalTime
    

    cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
 
    

    
