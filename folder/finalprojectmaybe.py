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
CamAng = v.vector(0,m.pi/2,0,'row')
#spherical coordinates for a unit vector
CamPoint = v.vector(0,0,0,'row')
#unit vector where cam points
CrossCam = v.vector(0,0,0,'row')
#vector pointing perpendicular to CamPoint
CamFOVSide = m.pi/4
CamFOVVertical = m.pi/6
CamXSensitivity = 1
#how fast the camera moves horizontally
CamYSensitivity = 1
#hot fast the camera moves vertically


def UpdateCamPoint():
    global CamPoint
    global CamAng
    global CrossX
    global CrossY
    CamPoint = v.vector(m.cos(CamAng.e0)*m.sin(CamAng.e1),m.sin(CamAng.e0)*m.sin(CamAng.e1),m.cos(CamAng.e1),'row')
    Vector1 = v.vector(m.cos(CamAng.e0)*m.sin(CamAng.e1 + m.pi/2),m.sin(CamAng.e0)*m.sin(CamAng.e1 + m.pi/2),m.cos(CamAng.e1 + m.pi/2),'row')
    Vector2 = v.vector(m.cos(CamAng.e0 + m.pi/2)*m.sin(CamAng.e1),m.sin(CamAng.e0 + m.pi/2)*m.sin(CamAng.e1),m.cos(CamAng.e1),'row')
    CrossX = v.cross(Vector1,CamPoint)
    CrossY = v.cross(Vector2,CamPoint)
    #print(CamPoint.comp)
    #print(Vector1.comp)
    #print(CrossCam.comp)
    
UpdateCamPoint()


def UpdateImage():
    global turt
    global CamPos
    global CamPoint
    global CrossX
    global CrossY
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
            Diff = v.subtract(CamPos,linelist)
            Cross = v.add(CrossX,CrossY)
            d = 1
            x = 0
            for iteration in range(1,10):
                difference1 = v.mag(Diff) - v.mag(v.add(v.scalarmult(d,CamPoint),v.scalarmult(m.sqrt(v.mag(Diff)**2 - d**2),Cross))) 
                if difference1 == 0:
                    break
                if difference1 < 0:
                    d += difference1/iteration
                elif difference1 > 0:
                    d += -difference1/iteration
            #print(str(difference1) +' '+'hi')
            for iteration in range(1,10):
                #print(iteration)
                #print(x)
        
                difference2 = v.mag(v.subtract(Diff,v.add(v.scalarmult(d,CamPoint),v.add(v.scalarmult(x,CrossX),v.scalarmult(m.sqrt(difference1**2-x**2),CrossY))))) 
                if difference2 == 0:
                    break
                if iteration == 1:
                    x += difference1/2
                    difference3 = v.mag(v.subtract(Diff,v.add(v.scalarmult(d,CamPoint),v.add(v.scalarmult(x,CrossX),v.scalarmult(m.sqrt(difference1**2-x**2),CrossY))))) 
                    x = 0
                    difference4 = difference2 - difference3
                    x += difference4/iteration
                else:
                    x += difference4/iteration
                    difference3 = v.mag(v.subtract(Diff,v.add(v.scalarmult(d,CamPoint),v.add(v.scalarmult(x,CrossX),v.scalarmult(m.sqrt(difference1**2-x**2),CrossY))))) 
                    x += -difference4/iteration
                    difference4 = difference2 - difference3
                    x += difference4/iteration
            y = m.sqrt(difference1**2 - x**2)
            
            if index1 == 0:
                turt.up()
                #turt.stamp()
                turt.goto(x,y)
            else:
                turt.down()
                #turt.stamp()
                turt.goto(x,y)
                

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
    CamPos = v.add(CamPos,v.scalarmult(-10,CrossX))
    #print(CamPos.comp)
    UpdateCamPoint()
    UpdateImage()

def MoveCamLeft():
    global CamPos
    global CamPoint
    #print(CamPos.comp)
    CamPos = v.add(CamPos,v.scalarmult(10,CrossX))
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




            


