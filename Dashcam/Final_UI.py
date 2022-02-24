import tkinter as tk
import cv2
from PIL import Image, ImageTk
import torch
import torch.nn as nn
import numpy as np
from Yolonet import yoloFun
from Test_MobileNet import test

"""
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1000,
    display_height=540,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
"""

class videoStream:
    panel = None
    window = None
    camera = None
    width = None
    height = None
    begin = None



    def __init__(self):
        self.window = tk.Tk()
        self.window.title('video')
        #self.window.geometry("400x400")
        self.width, self.height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry('%dx%d+0+0' % (self.width,self.height))
        self.panel=tk.Label(self.window, bg = '#3266a8', height = int(self.height), width = int(self.width))
        self.panel.pack()
        self.selectCar()

        
        self.camera=cv2.VideoCapture(0)
        self.camera1()
        self.camera.release()
        self.window.mainloop()
           

           
    def showCamera(self, carClass):
        print(carClass)
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
        confidence = yoloFun()
        if confidence > 0.6:
            #Save picture t oall 10 classes                
            final = test()
            #print(test)
            if (carClass == final):
                print("MATCH!")
                match = tk.Label(text = "MATCH!")
                match.config(font=("Courier", 100))
                match.place(x=self.width/1.7, y=self.height/1.5)
                """
    def searchCar(self, carClass):   
        if(carClass == 0):
            search = tk.Label(text = "Searching for \nAccura...")
            search.config(font=("Courier", 50))
            search.place(x=self.width/2, y=self.height/2)   
        self.showCamera(carClass)
                """
    def selectCar(self):
        wSpace = (self.width / 5) * 1.1
        hSpace = self.height / 5
        """
        Left Column
        """
        Screen = tk.Button(text = "Blank")
        Screen.config(font=("Courier", 35))
        #Screen.place(x=50, y=50)
        Acura = tk.Button(text = "  Acura   ", command = lambda : self.showCamera(0))
        Acura.config(font=("Courier", 35))
        #Acura.place(x=self.width/2.4, y=self.height/2.25)
        Acura.place(x=0, y=0)
        #red.pack()
        AM = tk.Button(text = "  Aston   ", command = lambda : self.showCamera(1))
        AM.config(font=("Courier", 35))
        #AM.place(x=self.width/2.6, y=self.height/1.825)
        AM.place(x=0, y=hSpace)
        #Blue.pack()
        BMW = tk.Button(text = "   BMW    ", command = lambda : self.showCamera(2))
        BMW.config(font=("Courier", 35))
        #Black.pack()
        #BMW.place(x=self.width/2.4, y=self.height/1.525)
        BMW.place(x=0, y=hSpace*2)
        #choose.destroy()
        Dodge = tk.Button(text = "  Dodge   ", command = lambda : self.showCamera(3))
        Dodge.config(font=("Courier", 35))
        Dodge.place(x=0, y=hSpace*3)
        Ford = tk.Button(text = " Ford SUV ", command = lambda : self.showCamera(4))
        Ford.config(font=("Courier", 35))
        Ford.place(x=0, y=hSpace*4)            
        """
        Right Column
        """
        Honda = tk.Button(text = "  Honda   ", command = lambda : self.showCamera(5))
        Honda.config(font=("Courier", 35))
        #Acura.place(x=self.width/2.4, y=self.height/2.25)
        Honda.place(x=wSpace, y=0)
        #red.pack()
        Jeep = tk.Button(text = "   Jeep   ", command = lambda : self.showCamera(6))
        Jeep.config(font=("Courier", 35))
        #AM.place(x=self.width/2.6, y=self.height/1.825)
        Jeep.place(x=wSpace, y=hSpace)
        #Blue.pack()
        Linc = tk.Button(text = " Lincoln  ", command = lambda : self.showCamera(7))
        Linc.config(font=("Courier", 35))
        #Black.pack()
        #BMW.place(x=self.width/2.4, y=self.height/1.525)
        Linc.place(x=wSpace, y=hSpace*2)
        #choose.destroy()
        Merc = tk.Button(text = " Mercedes ", command = lambda : self.showCamera(8))
        Merc.config(font=("Courier", 35))
        Merc.place(x=wSpace, y=hSpace*3)
        Volk = tk.Button(text = "Volkswagon", command = lambda : self.showCamera(9))
        Volk.config(font=("Courier", 35))
        Volk.place(x=wSpace, y=hSpace*4)        
    
    
    def camera1(self):
        
        """
        frameA = tk.frame(tk.master())
        
        """
        
        #self.camera=cv2.VideoCapture(0)
        _,frame=self.camera.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=Image.fromarray(frame)
        frame=ImageTk.PhotoImage(frame)
        
        
        
        self.panel.configure(image=frame)
        self.panel.image=frame
        self.panel.after(1,self.camera1)



if __name__ == '__main__':
        objVideo=videoStream()
    
    
"""

import tkinter
#import cv2
from PIL import Image, ImageTk

def showCamera():
    #root = tkinter.Tk()
    image1 = Image.open('White_Honda_Civic.jpg')
    test = ImageTk.PhotoImage(image1)
    
    label1 = tkinter.Label(image=test)
    label1.image = test
    
    # Position image
    window.minsize(1900, 1000)
    label1.place(x=0, y=0)
    window.mainloop()

def selectCar():
    empty = tkinter.Button(text = "               ")
    empty.pack()
    red = tkinter.Button(text = "Red Mustang", command = showCamera)
    red.config(font=("Courier", 35))
    red.place(x=width/2.4, y=height/2.25)
    #red.pack()
    Blue = tkinter.Button(text = "Blue Mitsubishi", command = showCamera)
    Blue.config(font=("Courier", 35))
    Blue.place(x=width/2.6, y=height/1.825)
    #Blue.pack()
    Black = tkinter.Button(text = "Black Mazda", command = showCamera)
    Black.config(font=("Courier", 35))
    #Black.pack()
    Black.place(x=width/2.4, y=height/1.525)
    choose.destroy()
    empty.destroy()

window = tkinter.Tk()
window.configure(bg='#3266a8')
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
print(width/2)

greeting = tkinter.Label(text = "Welcome to the AI Dashcam")
greeting.config(font=("Courier", 50))
greeting.place(x=width/4, y=height/4)
#greeting.pack()
begin = tkinter.Button(text = "Show Camera", command = showCamera)
begin.config(font=("Courier", 35))
#begin.pack()
begin.place(x=width/2.4, y=height/2.9)

choose = tkinter.Button(text = "Select a Car", command = selectCar)
choose.config(font=("Courier", 35))
#choose.pack()
choose.place(x=width/2.45, y=height/2.25)
#window.minsize(300, 300)
window.mainloop()


"""
    
    
    
    
    
    
