import Asteroid_v7 as ast

try:
   import maya.cmds as cmds   
except:
   pass

def Scale():
    name = cmds.ls(selection=True)[0]
    X = cmds.intFieldGrp(ScaleX, q=True, v=True)[0]
    Y = cmds.intFieldGrp(ScaleY, q=True, v=True)[0]
    Z = cmds.intFieldGrp(ScaleZ, q=True, v=True)[0]
    print X,Y,Z
    ast.asteroid_size(X,Y,Z)

def play_slider_range():
   S_frame = cmds.intFieldGrp(play_slider,q=True, value1=True)
   F_frame = cmds.intFieldGrp(play_slider,q=True, value2=True)
   print min
   print max
   ast.play_back(S_frame, F_frame)

def delete_button():
    cmds.select(all=True)
    cmds.delete()
   
def run():
    cmds.play(f=True)

def ast_value():
    value = cmds.intSliderGrp(astSlider, q=True, v=True)
    print value
    value = int(value)
    ast.make_asteroid(value)
    
def crate_val():
    name = cmds.ls(selection=True)[0]
    craters = cmds.intSliderGrp(cratSlide, q=True, v=True)
    craters = int(craters)
    ast.rand_crater_size(name,craters)
    
def peak_val():
    name = cmds.ls(selection=True)[0]
    peaks = cmds.intSliderGrp(peakSlide, q=True, v=True)
    peaks = int(peaks)
    ast.rand_peak_size(name, peaks)
