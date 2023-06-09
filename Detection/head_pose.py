import cv2
import mediapipe as mp
import numpy as np
import time
from tkinter import messagebox
from Detection import data

def face_dir(frame):

  if(data.checkL == False):
      data.startL = time.mktime(time.localtime())
  if(data.checkR == False):
      data.startR = time.mktime(time.localtime())
  if(data.checkU == False):
      data.startU = time.mktime(time.localtime())
  if(data.checkD == False):
      data.startD = time.mktime(time.localtime())            

  data.endL = time.mktime(time.localtime())
  data.endR = time.mktime(time.localtime())  
  data.endD = time.mktime(time.localtime())  
  data.endU = time.mktime(time.localtime())    

  mp_face_mesh = mp.solutions.face_mesh
  face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

  mp_drawing = mp.solutions.drawing_utils

  drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


  

  
  image = frame

  start = time.time()

  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

  image.flags.writeable = False

  results = face_mesh.process(image)

  image.flags.writeable = True

  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

  img_h, img_w, img_c = image.shape
  face_3d = []
  face_2d = []

  if results.multi_face_landmarks:

      for face_landmarks in results.multi_face_landmarks:
          for idx, lm in enumerate(face_landmarks.landmark):
              if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                  if idx == 1:
                      nose_2d = (lm.x * img_w, lm.y * img_h)
                      nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)
                  

                  x, y = int(lm.x * img_w), int(lm.y * img_h)

                    # Get the 2D Coordinates
                  face_2d.append([x, y])

                    # Get the 3D Coordinates
                  face_3d.append([x, y, lm.z])       
            
          face_2d = np.array(face_2d, dtype=np.float64)

          face_3d = np.array(face_3d, dtype=np.float64)

          focal_length = 1 * img_w

          cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                    [0, focal_length, img_w / 2],
                                    [0, 0, 1]])

          dist_matrix = np.zeros((4, 1), dtype=np.float64)

          success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

          rmat, jac = cv2.Rodrigues(rot_vec)

          angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

          x = angles[0] * 360
          y = angles[1] * 360
          z = angles[2] * 360
          
          
            
          if y < -10:
              text = "Looking Left"
              print(text)
              print(data.Left)
              data.checkL = True
              if(data.endL - data.startL >= 2):
                data.Left = data.Left + 1
                data.checkL = False
             
          elif y > 10:
              text = "Looking Right"
              print(text)
              print(data.Right)
              data.checkR = True
              if(data.endR - data.startR >= 2):
                data.Right = data.Right + 1
                data.checkR = False

          elif x < -10:
              text = "Looking Down"
              print(text)
              print(data.down)
              data.checkD= True
              if(data.endD - data.startD >= 2):
                data.down = data.down + 1
                data.checkD = False
              
          elif x > 10:
              text = "Looking up"
              print(text)
              print(data.up)
              data.checkU = True
              if(data.endU - data.startU >= 2):
                data.up = data.up + 1
                data.checkU = False
          else:
              text = "Forward"
              
              data.checkL = False
              data.checkR = False
              data.checkU = False
              data.checkD = False
             

          nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

          p1 = (int(nose_2d[0]), int(nose_2d[1]))
          p2 = (int(nose_2d[0] + y * 10) , int(nose_2d[1] - x * 10))
            
          cv2.line(image, p1, p2, (255, 0, 0), 3)

        

      
      end = time.time()
      totalTime = end - start

      fps = 1 / totalTime

      
      
      mp_drawing.draw_landmarks(
                  image=image,
                  landmark_list=face_landmarks,
                  connections=mp_face_mesh.FACEMESH_CONTOURS,
                  landmark_drawing_spec=drawing_spec,
                  connection_drawing_spec=drawing_spec)


    


  
