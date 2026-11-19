import math as m
import tkinter as tk
import Vectors as v
from pynput import keyboard
import turtle as tt

turt = tt.Turtle()
turt.hideturtle()
screen = tt.Screen()
turt.speed(0)
turt.up()


    
#root = tk.Tk()
#root.title('thingy')
#root.geometry('620x480')
#Def Angles(v):  
    #ang = vector(0,0,0)
    #for

CamPos = v.vector(100,100,50,'row')
CamAng = v.vector(0,m.pi/2,'row')
#spherical coordinates for a unit vector
CamPoint = v.vector(0,0,0,'row')
#unit vector where cam points
CrossCam = v.vector(0,0,0,'row')
#vector pointing perpendicular to CamPoint
CamFOVSide = m.pi/4
CamFOVVertical = m.pi/6
CamXSensitivity = 10
#how fast the camera moves horizontally
CamYSensitivity = 10
#hot fast the camera moves vertically


def UpdateCamPoint():
    global CamPoint
    global CamAng
    global CrossCam
    CamPoint = v.vector(m.cos(CamAng.e0)*m.sin(CamAng.e1),m.sin(CamAng.e0)*m.sin(CamAng.e1),m.cos(CamAng.e1),'row')
    Vector1 = v.vector(m.cos(CamAng.e0)*m.sin(CamAng.e1 + m.pi/2),m.sin(CamAng.e0)*m.sin(CamAng.e1 + m.pi/2),m.cos(CamAng.e1 + m.pi/2),'row')
    CrossCam = v.cross(Vector1,CamPoint)
    #print(CamPoint.comp)
    #print(Vector1.comp)
    #print(CrossCam.comp)
    
UpdateCamPoint()


def UpdateImage():
    global turt
    global CamPos
    global CamPoint
    turt.hideturtle()
    screen.reset()
    turt.hideturtle()
    screen.tracer(0)
    ObjectFile = open('PythonProjectData.txt')
    for index1,line in enumerate(ObjectFile):
        linelist = line.split(',')
        #print(linelist)
        linelist[-1] = linelist[-1][0:-1]
        #print(linelist)
        #print('hi')
        if len(linelist) != 1:
            for index,value in enumerate(linelist):
                #print(value)
                linelist[index] = float(value)
            #print(tuple(linelist))
            linelist.append('row')
            linelist = v.vector(tuple(linelist))
            #print(linelist)
            p = v.subtract(linelist,CamPos)
            c = v.subtract(p,v.scalarmult(v.mag(p)*m.cos(v.angle(p,CamPoint)),CamPoint))
            print(c.comp)
            if index1 == 0:
                turt.up()
                #turt.stamp()
                turt.goto(c.e0,c.e1)
            else:
                turt.down()
                turt.stamp()
                turt.goto(c.e0,c.e1)
                

            #turt.goto(2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVSide),2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVVertical)
            screen.update()
            
        
UpdateImage()


def MoveCamForward():
    global CamPos
    global CamPoint
    #print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CamPoint))
    #print(CamPos.comp)
    UpdateImage()

def MoveCamBackward():
    global CamPos
    global CamPoint
    #print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(-10,CamPoint))
    #print(CamPos.comp)
    UpdateImage()

def MoveCamRight():
    global CamPos
    global CamPoint
    #print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(-10,CrossCam))
    #print(CamPos.comp)
    UpdateCamPoint()
    UpdateImage()

def MoveCamLeft():
    global CamPos
    global CamPoint
    #print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CrossCam))
    #print(CamPos.comp)
    UpdateCamPoint()
    UpdateImage()

def PanCamUp():
    global CamAng
    global CamPoint
    #print(CamPoint.comp)
    if CamAng.e1 != 0 and not(CamAng.e1 - CamYSensitivity*m.pi/180 < 0):
        CamAng = v.vector(CamAng.e0,CamAng.e1 - CamYSensitivity*m.pi/180,'row')
    #print(CamPoint.comp)
    UpdateCamPoint()
    UpdateImage()
    
def PanCamDown():
    global CamAng
    global CamPoint
    #print(CamPoint.comp)
    if CamAng.e1 != m.pi and not(CamAng.e1 + CamYSensitivity*m.pi/180 > m.pi):
        CamAng = v.vector(CamAng.e0,CamAng.e1 + CamYSensitivity*m.pi/180,'row')
    #print(CamPoint.comp)
    UpdateCamPoint()
    UpdateImage()
    
def PanCamRight():
    global CamAng
    global CamPoint
    #print(CamPoint.comp)
    CamAng = v.vector(CamAng.e0 - CamXSensitivity*m.pi/180,CamAng.e1,'row')
    UpdateCamPoint()
    #print(CamPoint.comp)
    UpdateImage()
    
def PanCamLeft():
    global CamAng
    global CamPoint
    #print(CamPoint.comp)
    CamAng = v.vector(CamAng.e0 + CamXSensitivity*m.pi/180,CamAng.e1,'row')
    UpdateCamPoint()
    #print(CamPoint.comp)
    UpdateImage()
    


screen.listen()
screen.onkeypress(MoveCamForward,'w')
screen.onkeypress(MoveCamBackward,'s')
screen.onkeypress(MoveCamRight,'d')
screen.onkeypress(MoveCamLeft,'a')
screen.onkeypress(PanCamUp,'Up')
screen.onkeypress(PanCamDown,'Down')
screen.onkeypress(PanCamRight,'Right')
screen.onkeypress(PanCamLeft,'Left')




            


