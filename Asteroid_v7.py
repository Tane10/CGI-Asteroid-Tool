#! /usr/bin/python
# edit via music(this is an idea use sound modules)
''' Module of procedures to generate Asteroids
    type in 'ast.' before each module to run them
    
   This is script allows you to create custom asteroids using procedures like peak amount and crater number.
   After asteroid creation you can choses to apply collisions to your asteroids, this will allow you to become
   more realistic as well as give you an opportunity to test simulations with your custom asteroids
   
   This module contains the following procedures:

   asteroid_size   : Creates as many asteroids as you state.
   collisons
   make_asteroid   : Set size of the asteroid (height, width and depth).
   movement        : State the number of craters you would like on the asteroid.
   rand_crater_size: Randomises the size of craters using (height, width, depth).
   rand_peak_size  : Randomises the size of the peaks (height, width, depth).
   crack_asteroid  : Splits asteroid.
   
   The idea behind the module is to create custom asteroids, using a GUI interface.
   
   Example:
   
   >>>import maya.cmds as cmds
   >>>import Asteroids 
   
'''
##### can use GUI and let the user tell whick asteroids he wants to colide

import random as rnd

try:
   import maya.cmds as cmds   
except:
   pass

def make_asteroid(numb): #Working (tested 17/03/2014)
   
   '''Creates a sphere, then random changes the radius as well as set the sud div
      to a range between 40-100.
      
      On Exit: Creates an objects with the name asteroid and names the them in number iteration i.e. asteroid1, asteroid2 etc.
      
      For Example:
      
      >>> import maya.cmds as cmds
      >>> import random as rnd
      >>> 
      >>> cmds.polySphere(name='asteroid', sx= rnd.randint(40,200), sy= rnd.randint(40,200), r= rnd.randint(1,5))
      >>> for i in range(0,10):
      ...   cmds.duplicate('asteroid', name='asteroid' + str(i))
      ...   cmds.move(11*i,0,0, 'asteroid' + str(i))
      >>> cmds.delete('asteroid')
      >>>
      
      2 for loops one inside other
      out side loop reads every frame, inside one goes thought each asteroid

      
  '''
  
   numb = int(numb)   
   
   cmds.polySphere(name='asteroid', sx= rnd.randint(40,200), sy= rnd.randint(40,200), r= rnd.randint(1,5))
   for i in range(0,numb):
      cmds.duplicate('asteroid', name='asteroid' + str(i))
      cmds.move(11*i,0,0, 'asteroid' + str(i))
   cmds.delete('asteroid')

def asteroid_size(X,Y,Z): #Working (tested 17/03/2014) (still needs some editting)
 
 '''Allows the user to input numbers to change the scale of there Asteroid effecting
    the X, Y and Z.
    
    For example:
    
    >>> import maya.cmds as cmds
    >>>
    >>> cmds.polySphere(name = 'asteroid', sx= 40, sy= 40, r=10)
    >>> 
    >>> def Size():
    >>>     X = raw_input('Scale in the X axis.)
    >>>     X = int(X)
    >>>     
    >>>     Y = raw_input('Scale in the Y axis.)
    >>>     Y = int(Y)
    >>>     
    >>>     Z = raw_input('Scale in the Z axis.)
    >>>     Z = int(Z)
    >>>
    >>>     cmds.select(name)
    >>>     cmds.scale(X,Y,Z)
    >>>
    >>> AsteroidSize('asteroid')
    
 ''' 

 
 cmds.scale(X, Y, Z)
    
def rand_crater_size(name,craters): #Working (tested 17/03/2014) (add a while loop for question, fine tune code)
   
   '''Changes the crater size by adjusting the fallout and the depth of the crater allowing you to
      randomise the variables.
       
      For example:
      
      >>> import maya.cmds as cmds
      >>> import random
      >>> 
      >>> cmds.softSelect(sse=1,ssd=random.randint(0,10),ssc='1,1,2,0.0449282,1,2,2',ssf=2)
      >>> cmds.select('box.vtx[30]')
      >>>
      >>> center=[]
      >>> print center
      >>> 
      >>> X = cmds.objectCenter('asteroid', x=True, gl=True)
      >>> X = float(X)
      >>> center.append(X)
      >>> 
      >>> Y = cmds.objectCenter('asteroid', y=True, gl=True)
      >>> Y = float(Y)
      >>> center.append(Y)
      >>>  
      >>> Z = cmds.objectCenter('asteroid', z=True, gl=True)
      >>> Z = float(Z)
      >>> center.append(Z)
      >>> 
      >>> print center
      >>> 
      >>> cmds.spaceLocator(name= 'center', p=[center[0],center[1],center[2]])
      >>> 
      >>> craters = raw_input('How many crater would you like?)
      >>> craters = int(craters) 
      >>>
      >>> for i in range( 0, craters ):
      ...     the_vert = str( rnd.randint(0, len( points )/3) )
      ...     cmds.select('asteroid.vtx['+the_vert+']', replace=True)
      ...     cmds.select('center', add=True)
      ...     cmds.scale( 0.9, 0.9, 0.9, r=True )
      >>>
      
   '''
   
   cmds.softSelect(sse=1,ssd=3, ssc="1,0,1,0.75,0.25,1,0.5,0.5,1,0.75,0.25,1,0.25,0.75,1,1,0.249,1,0.749,0.499,1,0.499,0.749,1,0.257576,0.638554,1,0.530303,0.36747,1,0.348485,0.433735,1,0.409091,0.253012,1",ssf=1)
   
   all_points = cmds.select(name + '.vtx[:]') # selects every vert on the asteroid
 
   # finds out the translation of the verts
   points = cmds.xform(name  + '.vtx[:]', q=True, t=True, ws=True) 
   
   center=[] #makes empty list
       
   X = cmds.objectCenter(name, x=True, gl=True)#finds ceter in x axis
   X = float(X) #converts to a floats
   center.append(X) #appeds list adds x into list
           
   Y = cmds.objectCenter(name , y=True, gl=True)#fids center in Y
   Y = float(Y) #converts to float
   center.append(Y) #adds to list
           
   Z = cmds.objectCenter(name , z=True, gl=True)
   Z = float(Z)
   center.append(Z)

   cmds.spaceLocator( name='center', p=[center[0],center[1],center[2]])
 
   for i in range( 0, craters ):
      cmds.refresh()
      the_vert = str( rnd.randint(0, len( points )/3) )
      cmds.select(name + '.vtx['+the_vert+']', replace=True)
      cmds.select('center', add=True)
      cmds.scale( 0.955,0.955,0.955, r=True ) # scales points in to make the craters
      
   else:
      cmds.delete('center')
      cmds.delete(name , ch=True)

def rand_peak_size(name,peaks): #Working (tested 17/03/2014) (add a while loop for question, fine tune code)
   
   '''Changes the crater size by adjusting the fallout and the depth of the crater allowing you to
      randomise the variables.
       
      For example:
      
      >>> import maya.cmds as cmds
      >>> import random
      >>> 
      >>> cmds.softSelect(sse=1,ssd=random.randint(0,10),ssc='1,1,2,0.0449282,1,2,2',ssf=2)
      >>> cmds.select('box.vtx[30]')
      >>>
      >>> center=[]
      >>> print center
      >>> 
      >>> X = cmds.objectCenter('asteroid', x=True, gl=True)
      >>> X = float(X)
      >>> center.append(X)
      >>> 
      >>> Y = cmds.objectCenter('asteroid', y=True, gl=True)
      >>> Y = float(Y)
      >>> center.append(Y)
      >>> 
      >>> 
      >>> Z = cmds.objectCenter('asteroid', z=True, gl=True)
      >>> Z = float(Z)
      >>> center.append(Z)
      >>> 
      >>> print center
      >>> 
      >>> cmds.spaceLocator(name= 'center', p=[center[0],center[1],center[2]])
      >>> 
      >>> craters = raw_input('How many crater would you like?)
      >>> craters = int(craters) 
      >>>
      >>> for i in range( 0, craters ):
      ...     the_vert = str( rnd.randint(0, len( points )/3) )
      ...     cmds.select('asteroid.vtx['+the_vert+']', replace=True)
      ...     cmds.select('center', add=True)
      ...     cmds.scale( 0.9, 0.9, 0.9, r=True )
      >>>
      
   '''
   
   '''
      use import random as libary then add this with xform in a loop to get the heights
      this combo makes a nice montain peak
      softSelectCurve "0,1,0,1,0,1,0,1,1,0.939394,0.0722892,1,0.80303,0.138554,1,0.621212,0.180723,1,0.484848,0.240964,1,0.409091,0.295181,1,0.242424,0.379518,1,0.151515,0.5,1,0.136364,0.60241,1,0.212121,0.668675,1,0.166667,0.728916,1,0.0757576,0.771084,1,0.19697,0.819277,1,0.30303,0.855422,1,0.19697,0.885542,1,0.121212,0.933735,1,0.19697,0.96988,1";
      softSelectCurve "1,0,0,0,1,2,0.333333,0.0903614,0,0.909091,0.0783133,0,0.80303,0.060241,0,0.818182,0.126506,0,0.787879,0.168675,0,0.787879,0.222892,0,0.727273,0.271084,0,0.606061,0.253012,0,0.560606,0.216867,0,0.666667,0.192771,0,0.545455,0.156627,0,0.636364,0.307229,0,0.560606,0.355422,0,0.469697,0.36747,0,0.560606,0.39759,0,0.712121,0.475904,0,0.848485,0.403614,0,0.681818,0.421687,0,0.606061,0.463855,0,0.545455,0.433735,0,0.666667,0.518072,0,0.515152,0.518072,0,0.5,0.554217,0,0.5,0.608434,0,0.409091,0.572289,0,0.469697,0.680723,0,0.378788,0.674699,0,0.530303,0.650602,0,0.348485,0.63253,0,0.454545,0.759036,0,0.651515,0.73494,0,0.515152,0.795181,0,0.727273,0.777108,0,0.393939,0.813253,0,0.363636,0.879518,0,0.575758,0.837349,0,0.530303,0.89759,0,0.439394,0.927711,0,0.181818,0.921687,0,0.257576,0.96988,0"
      
      
      could use recution to grab single verts all over to make rocky effect
      
      For example:
      
      >>> import maya.cmds as cmds
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      
      cmds.softSelect(sse=1,ssd=3,ssc="1,0.3422,2,1,2,0,2,0.3333,0.599654,0.439,0.728,2,0.13,0.52,2,0.566933",ssf=1)
      cmds.softSelect(sse=1,ssd=3,ssc="0,1.88373,0,0.469697,0.0722892,2,0.818182,0.271084,15878,0.636364,0.740964,0,0.484848,0.855422,0,0,0.945783,0",ssf=1)
 '''
  
   # finds the translation of the asteroid
   place = cmds.getAttr(name + '.t', t=True)
   
   # selects all points on the asteroid
   all_points = cmds.select(name + '.vtx[:]')
   points = cmds.xform(q=True, t=True, ws=True)
   
   # creates a locator in the center of the object in the world space
   cmds.spaceLocator( name='center', p=[0,0,0] )

   for i in range( 0,peaks):
      cmds.refresh()
      the_vert = str( rnd.randint(0, len( points )/3) )
      cmds.select(name + '.vtx['+the_vert+']', replace=True)
      cmds.select('center', add=True)
      cmds.softSelect(sse=1,ssd=2,ssc="0,1,0,1,0,1,0,1,1,0.939394,0.0722892,1,0.80303,0.138554,1,0.621212,0.180723,1,0.484848,0.240964,1,0.409091,0.295181,1,0.242424,0.379518,1,0.151515,0.5,1,0.136364,0.60241,1,0.212121,0.668675,1,0.166667,0.728916,1,0.0757576,0.771084,1,0.19697,0.819277,1,0.30303,0.855422,1,0.19697,0.885542,1,0.121212,0.933735,1,0.19697,0.96988,1",ssf=1)
      cmds.scale( 1.12,1.12,1.12, r=True )
      cmds.softSelect(sse=1, ssd=2, ssc="1,0,0,0,1,2,0.333333,0.0903614,0,0.909091,0.0783133,0,0.80303,0.060241,0,0.818182,0.126506,0,0.787879,0.168675,0,0.787879,0.222892,0,0.727273,0.271084,0,0.606061,0.253012,0,0.560606,0.216867,0,0.666667,0.192771,0,0.545455,0.156627,0,0.636364,0.307229,0,0.560606,0.355422,0,0.469697,0.36747,0,0.560606,0.39759,0,0.712121,0.475904,0,0.848485,0.403614,0,0.681818,0.421687,0,0.606061,0.463855,0,0.545455,0.433735,0,0.666667,0.518072,0,0.515152,0.518072,0,0.5,0.554217,0,0.5,0.608434,0,0.409091,0.572289,0,0.469697,0.680723,0,0.378788,0.674699,0,0.530303,0.650602,0,0.348485,0.63253,0,0.454545,0.759036,0,0.651515,0.73494,0,0.515152,0.795181,0,0.727273,0.777108,0,0.393939,0.813253,0,0.363636,0.879518,0,0.575758,0.837349,0,0.530303,0.89759,0,0.439394,0.927711,0,0.181818,0.921687,0,0.257576,0.96988,0",ssf=1)
      cmds.scale( 1.069, 1.069,1.069, r=True )
      cmds.softSelect(sse=1, ssd=3.5, ssc="1,0,0,0,1,2,0.333333,0.0903614,0,0.909091,0.0783133,0,0.80303,0.060241,0,0.818182,0.126506,0,0.787879,0.168675,0,0.787879,0.222892,0,0.727273,0.271084,0,0.606061,0.253012,0,0.560606,0.216867,0,0.666667,0.192771,0,0.545455,0.156627,0,0.636364,0.307229,0,0.560606,0.355422,0,0.469697,0.36747,0,0.560606,0.39759,0,0.712121,0.475904,0,0.848485,0.403614,0,0.681818,0.421687,0,0.606061,0.463855,0,0.545455,0.433735,0,0.666667,0.518072,0,0.515152,0.518072,0,0.5,0.554217,0,0.5,0.608434,0,0.409091,0.572289,0,0.469697,0.680723,0,0.378788,0.674699,0,0.530303,0.650602,0,0.348485,0.63253,0,0.454545,0.759036,0,0.651515,0.73494,0,0.515152,0.795181,0,0.727273,0.777108,0,0.393939,0.813253,0,0.363636,0.879518,0,0.575758,0.837349,0,0.530303,0.89759,0,0.439394,0.927711,0,0.181818,0.921687,0,0.257576,0.96988,0",ssf=1)
      cmds.scale(0.99,0.99,0.99, r=True)
   else:
      cmds.delete('center')
      cmds.delete(name, ch=True)
  
def play_back(S_frame, F_frame): #edit

   '''This will allow you to move the asteroids around the world space and will call crack_asteroid
      when the asteroids reach each other simulating then splitting.
      
      S_frame: This varible is for the start key frame of the aimation.
      F_frame:  Allows you to add in a translate vaule when going to aniamte.
      
      For exaple: 
      
      >>> import maya.cmds as cmds
      >>> 
      >>> cmds.polySphere(name= 'asteroid', r=10, sx=100, sy=100)
      >>> cmds.exactWorldBoundingBox('asteroid')
      >>> bbox = cmds.exactWorldBoundingBox('asteroid1')
      >>> bbox2 = cmds.exactWorldBoundingBox('asteroid2') 
      >>> print bbox
      >>> print bbox2
      >>>  
      >>> ###collison dectection###
      >>> def test():
      ...   if (box[3] > box2[0] and
      ...   box[0] < box2[3] and
      ...   box[4] > box2[1] and
      ...   box[1] < box2[4] and
      ...   box[5] > box2[2] and
      ...   box[2] < box2[5]):
      ...      print 'yes'
      ...   else:
      ...      print 'nope'
      >>>
      >>> cmds.setKeyframe(v= value, t=time, )
      >>>
      >>> cmds.setKeyframe('box', at='translateX', v=10, t=['0sec','10sec'])
      >>>

   '''  
   cmds.playbackOptions(minTime= S_frame, maxTime= F_frame)
    
def colouision():#basicly duplicate and scale down
   '''This will simulate a cracking a asteroid using the scale and duplicate tool.
      it will call the above procedurs to edit the new asteroid and re name the crack as 'asteroid_i_cr
      
      VeloX : velocity X
      VeloY : velocity Y
      VeloZ : velocity Z
      
      
      >>>
      >>> for i in range(0,2):
      ...    cmds.select('asteroid' + str(i), add= True)
      ...    cmds.rigidBody(n='asteroid' + str(i) + '_RB', act = True, cl= True)
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      >>>
      http://www.joelstutz.com/Rigid%20bodies.html
      http://download.autodesk.com/global/docs/maya2014/en_us/index.html?url=files/Syntax_Command_syntax.htm,topicNumber=d30e806548
   '''
   '''
int $coll = 'rigidBody -q -cc rigidBody3';
if($coll >= 1)
{
	select pCube1;
	delete -ch;
	solidShatter("solidShatter", 3,1,1,0,0,0.5,0,3,"rigid bodies with collisions off",0,0);
}
for($i=1;$i<10;++$i)
{
    string $name;
    $name="rigidBody"+(string)$i+".collisions";
    
    string $whatever;
    $whatever="getAttr "+$name;
    
    if($whatever!="1")
    {
        setAttr $name 1;
    }
    else
    {
        print "nope";
    }    
}

mel code exprestion   
 '''  
   
   obj_ls = cmds.ls('asteroid*Shape')
   
   for i in range(0,len(obj_ls)):
      cmds.select('asteroid' + str(i), add= True)
      cmds.rigidBody(n= 'asteroid' + str(i) + '_RB', act= True, cl= True, iv= [0,0,0], cc=True)
   
  # bake in simulation when finished
   #for i in range(0, le)
