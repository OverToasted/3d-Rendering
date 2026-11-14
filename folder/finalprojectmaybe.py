import math as m
import tkinter as tk
import Vectors as v
from pynput import keyboard
import turtle as tt

turt = tt.Turtle()
turt.speed(0)
turt.up()
screen = tt.Screen()
    
#root = tk.Tk()
#root.title('thingy')
#root.geometry('620x480')
#Def Angles(v):  
    #ang = vector(0,0,0)
    #for 
CamPos = v.vector(100,100,50,'row')
CamPointAng = v.vector(1,1,m.pi/6,'row')
CamPoint = v.vector(0,1,0,'row')
def UpdateCamPoint():
    global CamPoint
    global CamPointAng
    CamPoint = v.vector(m.cos(CamPointAng.e0),m.cos(CamPointAng.e1),m.cos(CamPointAng.e2),'row')
    
UpdateCamPoint()
#vector contains cam angles in the pitch, yaw, and roll
CamFOVSide = m.pi/4
#degrees

CamFOVVertical = m.pi/6
#degrees

RightMatrix = v.matrix(v.vector(m.cos(m.pi/6),0,0,'row'),v.vector(0,m.sin(m.pi/6),0,'row'),v.vector(0,0,1,'row'))
LeftMatrix = v.matrix(v.vector(m.cos(-1*m.pi/6),0,0,'row'),v.vector(0,m.sin(-1*m.pi/6),0,'row'),v.vector(0,0,1,'row'))
RightVector = v.vector(m.pi/2,m.pi/2,0,'row')
LeftVector = v.vector(-1*m.pi/2,-1*m.pi/2,0,'row')
def UpdateImage():
    screen.reset()
    ObjectFile = open('PythonProjectData.txt')
    for line in ObjectFile:
        linelist = line.split(',')
        #print(linelist)
        linelist[-1] = linelist[-1][0:-1]
        #print(linelist)
        #print('hi')
        if len(linelist) == 1:
            print('')
        else:
            for index,value in enumerate(linelist):
                linelist[index] = float(value)
            #print(tuple(linelist))
            linelist.append('row')
            linelist = v.vector(tuple(linelist))
            #print(linelist)
            turt.goto(2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVSide)/(v.subtract(linelist,v.scalarmult(v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist)),CamPoint)).e0),2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVVertical)/(v.subtract(linelist,v.scalarmult(v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist)),CamPoint)).e1))
            turt.down()

            
def MoveCamForward():
    global CamPos
    global CamPoint
    print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CamPoint))
    print(CamPos.comp)
    UpdateImage()

def MoveCamBackward():
    global CamPos
    global CamPoint
    print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(-10,CamPoint))
    print(CamPos.comp)
    UpdateImage()

def MoveCamRight():
    global CamPos
    global CamPoint
    global CamPointAng
    CamPointAng = v.add(CamPointAng,RightVector)
    UpdateCamPoint()
    print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CamPoint))
    print(CamPos.comp)
    CamPointAng = v.add(CamPointAng,LeftVector)
    UpdateCamPoint()
    UpdateImage()

def MoveCamLeft():
    global CamPos
    global CamPoint
    global CamPointAng
    CamPointAng = v.add(CamPointAng,LeftVector)
    UpdateCamPoint()
    print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CamPoint))
    print(CamPos.comp)
    CamPointAng = v.add(CamPointAng,RightVector)
    UpdateCamPoint()
    UpdateImage()


        
UpdateImage()

screen.listen()
screen.onkeypress(MoveCamForward,'w')
screen.onkeypress(MoveCamBackward,'s')
screen.onkeypress(MoveCamRight,'d')
screen.onkeypress(MoveCamLeft,'a')



            


