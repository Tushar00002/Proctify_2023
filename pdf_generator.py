from fpdf import FPDF 
from Detection import data


def pdf_gen():
 ch = 50
 m= 10
 pw = 210-2*m

 pdf = FPDF()

 pdf.add_page()




 

 pdf.image('Assets\Images\ICON2_img.jpg',x = 5, y = 5, w = 20, h = 20, type = 'JPG')
 pdf.set_font('Arial', '', 36)
 pdf.cell(w=0, h=10,align='C', txt = "Proctify" + data.name,border=0, ln=1)
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 pdf.set_font('Arial', '', 12)
 # for info of user
 pdf.cell(w=3*pw/4, h=10, txt = "Name : " + data.name,border=1, ln=1)
 pdf.cell(w=3*pw/4, h=10, txt = "Registration N0.: "+ str(data.roll),border=1, ln=1)
 pdf.cell(w=3*pw/4, h=10, txt = "Test_URL :"+data.test_url,border=1, ln=1)

 # for procturing info
 pdf.cell(w=3*pw/8, h=10, txt = "Duration : 10 min",border=1, ln=0)
 pdf.cell(w=3*pw/8, h=10, txt = "Calculator : Enabled",border=1, ln=1)

 pdf.image('Nature.jpg',x = 6*pw/7, y = 40, w = pw/5, h = 40, type = 'JPG')

##############################################################################################


 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 # Head Movement
 # 
 if(data.Left!=0):
  pdf.set_fill_color(r=255,g=0,b=0)
 else:
  pdf.set_fill_color(r=0,g=255,b=0)
 pdf.cell(w=pw/2,fill=True, h=10, txt = "Suspicious Head Movement Left  : " + str(data.checkL),border=1, ln=0)

 if(data.Right!=0):
  pdf.set_fill_color(r=255,g=0,b=0)
 else:
  pdf.set_fill_color(r=0,g=255,b=0)
 pdf.cell(w=pw/2,fill=True,  h=10, txt = "Suspicious Head Movement Right   : "  + str(data.checkR),border=1, ln=1)

 if(data.up!=0):
  pdf.set_fill_color(r=255,g=0,b=0)
 else:
  pdf.set_fill_color(r=0,g=255,b=0)
 pdf.cell(w=pw/2,fill=True,  h=10, txt = "Suspicious Head Movement Up   : "  + str(data.checkU),border=1, ln=0)
 
 if(data.down!=0):
  pdf.set_fill_color(r=255,g=0,b=0)
 else:
  pdf.set_fill_color(r=0,g=255,b=0)
 pdf.cell(w=pw/2,fill=True,  h=10, txt = "Suspicious Head Movement Down  : "  + str(data.checkD),border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

###############################################################################################################


# Cell Phone


 pdf.set_text_color(r=255,g=255,b=255)
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.cell(w=pw/2, h=10,fill=True, txt = "Cell Phone Detected",border=1, ln=0)
 pdf.set_text_color(r=0,g=0,b=0) 

 pdf.set_text_color(r=255,g=255,b=255)
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.cell(w=pw/2, h=10,fill=True, txt = "Laptop Detected",border=1, ln=1)
 pdf.set_text_color(r=0,g=0,b=0) 
 pdf.cell(w=0, h=40, txt = "",border=2, ln=1)
  
 pdf.image(data.cell_url,x = 10, y = 135, w = pw/2, h = 40, type = 'JPG')
 pdf.image(data.lap_url,x = 105, y = 135, w = pw/2, h = 40, type = 'JPG')
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

# User Missing


 pdf.set_text_color(r=255,g=255,b=255)
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.cell(w=0, h=10,fill=True, txt = "User Out of Frame",border=1, ln=1)
 pdf.set_text_color(r=0,g=0,b=0)  

 pdf.image(data.img[0],x = 10, y = 195, w = pw/2, h = 40, type = 'JPG')
 pdf.image(data.img[1],x = 105, y = 195, w = pw/2, h = 40, type = 'JPG') 
 pdf.cell(w=0, h=50, txt = "",border=2, ln=1)
# for val in data.img:
  #  pdf.image(val,x = 10, y = None, w = pw/2, h = 40, type = 'JPG')
   
##################################################################################
# Multiple Face

 pdf.set_text_color(r=255,g=255,b=255)
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.cell(w=0, h=10,fill=True, txt = "Multiple Face Detected",border=1, ln=1)
 pdf.set_text_color(r=0,g=0,b=0)  
 pdf.cell(w=0, h=20, txt = "",border=2, ln=1)
 pdf.image(data.mul_img[0],x = 10, y = 255, w = pw/2, h = 40, type = 'JPG')
 pdf.image(data.mul_img[1],x = 105, y = 255, w = pw/2, h = 40, type = 'JPG')

  # for val in data.mul_img:
  #  pdf.image(val,x = 10, y = None, w = pw/2, h = 40, type = 'JPG')
###############################################################################################
# Tab Switch

 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.set_text_color(r=255,g=255,b=255)
 pdf.cell(w=0, h=10,fill=True, txt = "Tab Switch Detected",border=1, ln=1)
 pdf.set_text_color(r=0,g=0,b=0)
 pdf.image(data.sc_url[0],x = 10, y = 25, w = pw/2, h = 40, type = 'JPG')
 pdf.image(data.sc_url[1],x = 105, y = 25, w = pw/2, h = 40, type = 'JPG')
 pdf.cell(w=0, h=50, txt = "",border=2, ln=1)
######################################################################################

 

 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.set_text_color(r=255,g=255,b=255)
 pdf.cell(w=0, h=10,fill=True, txt = "Random Photo",border=1, ln=1) 
 pdf.set_text_color(r=0,g=0,b=0)
 pdf.image('Nature.jpg',x = 10, y = 85, w = pw/2, h = 40, type = 'JPG')
 pdf.image('Nature.jpg',x = 105, y = 85, w = pw/2, h = 40, type = 'JPG')
 pdf.cell(w=0, h=50,border=2, ln=1) 


#########################################################################################
# Background Apps
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.set_text_color(r=255,g=255,b=255)
 pdf.cell(w=0, h=10,fill=True, txt = "Background Apps Running",border=1, ln=1)
 pdf.set_text_color(r=0,g=0,b=0)
 for val in data.softwares:
  pdf.cell(w=pw/2, h=10, txt = val,border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
#######################################################################################
 if(data.tabswitch != True):
  pdf.set_fill_color(r=0,g=128,b=128)
  pdf.set_text_color(r=255,g=255,b=255)
  pdf.cell(w=0, h=10,fill=True, txt = "URL Visited",border=1, ln=1)
  pdf.set_text_color(r=0,g=0,b=0) 
  for val in data.URL:
   pdf.cell(w=pw/2, h=10, txt = val,border=1, ln=1)
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

####################################################################################### 
 # To be decided
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=0)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=1)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=0)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=1)




 pdf.set_xy(x=10, y= 220) # or use pdf.ln(50)


 pdf.output(f'./result.pdf','F')
 print('PDF Generated')

pdf_gen()