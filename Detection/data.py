import time
import collections

name =''
roll = 0

# Looking in any direction for more than 3 sec 
up = 0
startU = time.mktime(time.localtime())
endU =  time.mktime(time.localtime())
checkU = False

#Left
Left = 0
startL = time.mktime(time.localtime())
endL =  time.mktime(time.localtime())
checkL = False


down = 0
startD = time.mktime(time.localtime())
endD =  time.mktime(time.localtime())
checkD = False


Right = 0
startR = time.mktime(time.localtime())
endR =  time.mktime(time.localtime())
checkR = False



# Multiple Face

multiple_count = 0
mul_img = ['Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg']
img_mul = 0
# multiple face for time interval more than 4 sec
multi4 = 0
ismulti = False


# Object Detection
object_List = {'cell phone':0,'laptop':0}
res = collections.ChainMap(object_List)
cell_url = "Assets/Images/peakpx.jpg"
lap_url = "Assets/Images/peakpx.jpg"
pic1= 0
pic2 = 0




 # Array of object detected
isobject = False

#usermissing for more than 4 sec
start_miss = time.mktime(time.localtime())
end_miss =  time.mktime(time.localtime())
usermiss = 0
check_miss = False
img = ['Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg']
pic_taken = 0




check = False
start = time.mktime(time.localtime())
end =  time.mktime(time.localtime())
        
# Already running softwares

softwares = []

# URL visited
URL = set(())
sc_taken = 0
sc_url  = ['Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg','Assets/Images/peakpx.jpg']
switch = 0
tabswitch = False

test_url = 'https://www.tutorialspoint.com/index.htm'

#https://www.tutorialspoint.com/index.htm

# Checking if user has input his details or not
isregister = False


is_snap = False

is_proctor = False