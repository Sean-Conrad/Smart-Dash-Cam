# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:03:13 2021

@author: Zhiiaiin
"""

import torch
import torch.nn as nn
from Yolonet import yoloFun
from Test_MobileNet import test, modelLoad
import cv2
import numpy as np
import tkinter as tk
from PIL import Image,ImageTk
import datetime
import threading
import subprocess
from shutil import copyfile 


class windowInfo:
    width = 0
    height = 0
    model = None


def takePhoto():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save("Picture.jpg")

    
def beginSearch(carClass, W):
    
    #print(carClass)
    """
    if(carClass == 0):
            search = tk.Label(text = "Searching for \nAccura...")
            search.config(font=("Courier", 100))
            search.place(x=self.width/2, y=self.height/2)            
    """
    #take picture every 5 seconds
    #Save picture to YoloNet
    #Process to Yolonet
    #If confidence > 60% process to mobileNet
    
    path0 = "Car-Dataset/test/Acura/Picture.jpg"
    path1 = "Car-Dataset/test/Aston Martin/Picture.jpg"
    path2 = "Car-Dataset/test/BMW/Picture.jpg"
    path3 = "Car-Dataset/test/Dodge/Picture.jpg"
    path4 = "Car-Dataset/test/Ford SUV/Picture.jpg"
    path5 = "Car-Dataset/test/Honda Accord/Picture.jpg"
    path6 = "Car-Dataset/test/Jeep SUV/Picture.jpg"
    path7 = "Car-Dataset/test/Lincoln Sedan/Picture.jpg"
    path8 = "Car-Dataset/test/Mercedes-Benz Convertible/Picture.jpg"
    path9 = "Car-Dataset/test/Volkswagen Beetle/Picture.jpg"    
    
    
    #while carClass > -1:
    print("hello")
    threading.Thread(target = takePhoto()).start()
    
    
    #takePhoto()
    confidence = yoloFun()
      
    
    
    
        
    
    #confidence = 0.7
    if confidence > 0.6:
        
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Acura\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Aston Martin\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\BMW\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Dodge\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Ford SUV\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Honda Accord\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Jeep SUV\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Lincoln Sedan\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Mercedes-Benz Convertible\Picture.jpg")
        copyfile(r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Picture.jpg", 
                 r"C:\Users\bboys\Documents\School Work\SPR 21\ECE 397\Dashcam Code\ECE-397-Project-Dashcam-code\Car-Dataset\test\Volkswagen Beetle\Picture.jpg")

        
        
        #Save picture t oall 10 classes    
        final = test(W.model)
        #print(test)
        if (carClass == final):
            print("MATCH!")
            match = tk.Label(text = "   MATCH!   ")
            match.config(font=("Courier", 100))
            match.place(x=W.width/2.1, y=W.height/1.5)  #CHANGE  ME
    #root.after(1000, threading.Thread(target = beginSearch(carClass)).start())            
        else:
            print("NO MATCH!")
            match = tk.Label(text = "  NO MATCH! ")
            match.config(font=("Courier", 100))
            match.place(x=W.width/2.1, y=W.height/1.5)
            
            
            
    """
def searchCar(self, carClass):   
    if(carClass == 0):
        search = tk.Label(text = "Searching for \nAccura...")
        search.config(font=("Courier", 50))
        search.place(x=self.width/2, y=self.height/2)   
    self.showCamera(carClass)
            """
def selectCar(W):
    #wSpace = (700 / 5) * 1.1    #CHANGE ME
    #hSpace = 640 / 5
    
    wSpace = (W.width/5) * 1.1
    hSpace = W.height/5
    
    """
    Left Column
    """
    Screen = tk.Button(text = "Blank")
    Screen.config(font=("Courier", 35))
    #Screen.place(x=50, y=50)
    Acura = tk.Button(text = "  Acura   ", command = lambda : threading.Thread(target = beginSearch(0, W)).start())
    Acura.config(font=("Courier", 35))
    #Acura.place(x=self.width/2.4, y=self.height/2.25)
    Acura.place(x=0, y=0)
    #red.pack()
    AM = tk.Button(text = "  Aston   ", command = lambda : threading.Thread(target = beginSearch(1, W)).start())
    AM.config(font=("Courier", 35))
    #AM.place(x=self.width/2.6, y=self.height/1.825)
    AM.place(x=0, y=hSpace)
    #Blue.pack()
    BMW = tk.Button(text = "   BMW    ", command = lambda : threading.Thread(target = beginSearch(2, W)).start())
    BMW.config(font=("Courier", 35))
    #Black.pack()
    #BMW.place(x=self.width/2.4, y=self.height/1.525)
    BMW.place(x=0, y=hSpace*2)
    #choose.destroy()
    Dodge = tk.Button(text = "  Dodge   ", command = lambda : threading.Thread(target = beginSearch(3, W)).start())
    Dodge.config(font=("Courier", 35))
    Dodge.place(x=0, y=hSpace*3)
    Ford = tk.Button(text = " Ford SUV ", command = lambda : threading.Thread(target = beginSearch(4, W)).start())
    Ford.config(font=("Courier", 35))
    Ford.place(x=0, y=hSpace*4)            
    """
    Right Column
    """
    Honda = tk.Button(text = "  Honda   ", command = lambda : threading.Thread(target = beginSearch(5, W)).start())
    Honda.config(font=("Courier", 35))
    #Acura.place(x=self.width/2.4, y=self.height/2.25)
    Honda.place(x=wSpace, y=0)
    #red.pack()
    Jeep = tk.Button(text = "   Jeep   ", command = lambda : threading.Thread(target = beginSearch(6, W)).start())
    Jeep.config(font=("Courier", 35))
    #AM.place(x=self.width/2.6, y=self.height/1.825)
    Jeep.place(x=wSpace, y=hSpace)
    #Blue.pack()
    Linc = tk.Button(text = " Lincoln  ", command = lambda : threading.Thread(target = beginSearch(7, W)).start())
    Linc.config(font=("Courier", 35))
    #Black.pack()
    #BMW.place(x=self.width/2.4, y=self.height/1.525)
    Linc.place(x=wSpace, y=hSpace*2)
    #choose.destroy()
    Merc = tk.Button(text = " Mercedes ", command = lambda : threading.Thread(target = beginSearch(8, W)).start())
    Merc.config(font=("Courier", 35))
    Merc.place(x=wSpace, y=hSpace*3)
    Volk = tk.Button(text = "Volkswagon", command = lambda : threading.Thread(target = beginSearch(9, W)).start())
    Volk.config(font=("Courier", 35))
    Volk.place(x=wSpace, y=hSpace*4)    
    
    
W = windowInfo()   
root=tk.Tk()   
W.width, W.height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (W.width, W.height))

#oot.geometry("700x640")
root.configure(bg="black")
tk.Label(root,text="AI DASH CAM", font=("comic sans", 30, "bold"),bg="black",fg="blue").pack()
f1 = tk.LabelFrame(root,bg="red")
#f1.pack()
f1.place(x = W.width/1.6, y = 0)
L1=tk.Label(f1,bg="red")
L1.pack()

W.model = modelLoad() 
selectCar(W)
cap = cv2.VideoCapture(0)

tk.Button(root,text="Foxwire", font=("comic sans", 20, "bold"),bg="red",fg="blue", command=takePhoto).pack()

while True:
    
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    
    root.update()

cap.release()

