import math as m
import tkinter as tk
import Vectors as v
import pynput as pt
import turtle as tt

ObjectFile = open('PythonProjectData.txt')

turt = tt.Turtle()


#root = tk.Tk()
#root.title('thingy')
#root.geometry('620x480')
#Def Angles(v):  
    #ang = vector(0,0,0)
    #for 
CamPos = v.vector(0,0,0)
CamPoint = v.vector(90,0,0)#vector contains cam angles relative to [1,1,1]
CamFOV = 45 #degrees

