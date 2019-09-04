import Asteroid_GUI_Proceders as Pro
import Asteroid_v7 as ast

try:
   import maya.cmds as cmds   
except:
   pass

#check if window exists
if cmds.window('Asteroids', exists = True):
    cmds.deleteUI('Asteroids')
  
#create window
window = cmds.window('Asteroids', title = 'Asteroid Creator', w=300, h=500, mnb= True, mxb= False, sizeable= False)

#create main layout(row column layout)
mainLayout  = cmds.rowColumnLayout(nc= 1,columnWidth =[(1,350)])

#banner image
imagePath = cmds.internalVar(upd =True) + "icons/Asteroid_Creator.jpg"
cmds.image(w= 350, h= 150, image= imagePath)

#asteroid intslider
cmds.separator(h=5,style="in")
astSlider = cmds.intSliderGrp( field=True,label= "Number of Asteroids:           " ,min=0,max=30,v=0,cc="ast_value()")
cmds.separator(h=5,style="none")

#crater intslider  
cratSlide = cmds.intSliderGrp( field=True,label= "Number of Craters:              " ,min=0,max=400,v=0,cc="crate_val()")
cmds.separator(h=5,style="none")

#peaks intslider
peakSlide = cmds.intSliderGrp( field=True,label= "Number of Peaks:                " ,min=0,max=400,v=0, cc="peak_val()" )
cmds.separator(h=10, style='in')

#edit size text
cmds.text(label= "Edit size:")
cmds.separator(h=5,style= "none")

#Scale X,Y,Z
ScaleX = cmds.intFieldGrp(nf=1,label='Scale:                                 X',value1=0, cc="Scale()")
ScaleY = cmds.intFieldGrp(nf=1,label='Scale:                                 Y',value1=0, cc="Scale()")
ScaleZ = cmds.intFieldGrp(nf=1,label='Scale:                                 Z',value1=0, cc="Scale()")
cmds.separator(h=5, style='in')

#Play Slider range
cmds.separator(h=4,style="none")
play_slider = cmds.intFieldGrp(nf=2,label='Play slider range:                  ', value1=0,value2=0,cal=[1,'left'],cc="play_slider_range()")
cmds.separator(h=10,style="in")
   
#play button
cmds.button(label ="Play!!!",h=30, c="run()")

#collisions button
cmds.separator(h=10,style="in")
cmds.button(label ="Turn on Collisions", h=50,c="ast.colouision()")
cmds.separator(h=10,style="in")

#delete button
cmds.button(label= "Clear Scene",c="delete_button()")
cmds.separator(h=5,style="in")
#show window
cmds.showWindow(window)
