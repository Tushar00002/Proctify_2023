import cv2
from cv2 import imread
from cv2 import CascadeClassifier

#OpenCV provides the CascadeClassifier class that can be used to create a cascade classifier for face detection.

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("MORAYTA.mp4")

#Check if the video is opened correctly

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot Open Webcam")

#Pretrained Model
cascadeClassifier = CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    #Getting a frame from the webcam
    success,img = cap.read()
    #Usinf cascade classifier of opencv to detect faces
    bboxes = cascadeClassifier.detectMultiScale(img, 1.05, 8)
    count=0
    #Putting a box around every face
    for box in bboxes:
        count+=1
        x,y,width,height = box
        x2,y2 = x+width,y+height
        cv2.rectangle(img, (x,y), (x2,y2), (0,0,255), 2)
    #No of faces in the frame
    print(count)
    cv2.imshow("Output",img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()