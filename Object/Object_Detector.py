import cv2
import numpy as np
from Detection import data
import pyautogui
import time


thres = 0.6 # Threshold to detect object
nms_threshold = 0.2

#cap = cv2.VideoCapture("MORAYTA.mp4")

#Check if the video is opened correctly



classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def object(img):
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))
    

    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    

    for i in indices:
        
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)

        print(classNames[classIds[i]-1])
        if(classNames[classIds[i]-1] == 'cell phone'):
         data.object_List[classNames[classIds[i]-1]] = data.object_List[classNames[classIds[i]-1]] + 1
         if(data.pic1<1):
          data.cell_url ='ResultAssets/Cell/cell_phone'  + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
          cv2.imwrite('ResultAssets/Cell/cell_phone' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg",img)
          data.pic1 = data.pic1 + 1
        if(classNames[classIds[i]-1] == 'laptop'):
         data.object_List[classNames[classIds[i]-1]] = data.object_List[classNames[classIds[i]-1]] + 1 
         if(data.pic2<1):
          data.lap_url ='ResultAssets/Laptop/laptop'
          cv2.imwrite('ResultAssets/Laptop/laptop' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg",img)
          data.pic2 = data.pic2 + 1    
        cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),
        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    
        


