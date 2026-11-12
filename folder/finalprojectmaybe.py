import math as m
import tkinter as tk
import Vectors as v
import pynput as pt
import turtle as tt

ObjectFile = open('PythonProjectData.txt')

turt = tt.Turtle()
turt.up()

#root = tk.Tk()
#root.title('thingy')
#root.geometry('620x480')
#Def Angles(v):  
    #ang = vector(0,0,0)
    #for 
CamPos = v.vector(100,100,50,'row')
CamPoint = v.vector(m.pi/2,0.1,0.5,'row')
#vector contains cam angles in the pitch, yaw, and roll
CamFOVSide = m.pi/4
#degrees

CamFOVVertical = m.pi/6
#degrees

for line in ObjectFile:
    linelist = line.split(',')
    #print(linelist)
    linelist[-1] = linelist[-1][0:-1]
    #print(linelist)
    #print('hi')
    if len(linelist) == 1:
        print('new triangle')
    else:
        for index,value in enumerate(linelist):
            linelist[index] = float(value)
        #print(tuple(linelist))
        linelist.append('row')
        linelist = v.vector(tuple(linelist))
        #print(linelist)
        turt.goto(2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVSide)/(v.subtract(linelist,v.scalarmult(v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist)),CamPoint)).e0),2*v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist))*m.tan(CamFOVVertical)/(v.subtract(linelist,v.scalarmult(v.vectdist(CamPos,linelist)*m.cos(v.angle(CamPoint,linelist)),CamPoint)).e1))
        turt.down()

