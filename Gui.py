import tkinter as tk
import cv2, time
from PIL import Image, ImageTk
import numpy as np

"""
#Create an instance of tkinter frame
win = tk.Tk()
win.geometry("700x550")
#Load the image
img = cv2.imread('SpiderVerseBackground.png')

vid = cv2.VideoCapture(0)

ret, frame = vid.read()
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

im = Image.fromarray(frame)
imgtk = ImageTk.PhotoImage(image=im)

feed = tk.Label(win, image= imgtk)
feed.pack()

while True:
    ret, frame = vid.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    im = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=im)

    #Create a Label to display the image
    feed.configure(image= imgtk)
    win.update()
"""

"""
I want to use multiple windows for the differant functions of the program.

In dev order...
1. Livefeed
2. Capture
3. Timeline
4. Settings
5. File Management
"""

class LiveFeed:
    def __init__(self, size):
        self.size = size
        self.cam = 0
        self.vid = cv2.VideoCapture(self.cam)
    
    def nextFrame(self):
        captured, frame = self.vid.read()
        if captured:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        else:
            frame = np.zeros((self.size[0],self.size[1],3), np.uint8)

        return frame

    def saveFrame(self):
        # get the frame
        frame = self.nextFrame()
        dim = frame.shape

        # crop the image to the same ratio as the feed size
        if self.size[0]/dim[1] > self.size[1]/dim[0]:
            ratio = self.size[0]/dim[1]
        else:
            ratio = self.size[1]/dim[0]
        
        # find the height and width of the final image
        width = self.size[0]/ratio
        height = self.size[1]/ratio 

        cropped = frame[0:int(height), 0:int(width)]

        # return the cropped image
        return cropped
    
    def showFrame(self):
        # get the frame
        frame = self.nextFrame()
        dim = frame.shape

        # crop the image to the right size
        if self.size[0]/dim[1] > self.size[1]/dim[0]:
            ratio = self.size[0]/dim[1]
        else:
            ratio = self.size[1]/dim[0]
        # find the height and width of the corrected ratio
        width = self.size[0]/ratio
        height = self.size[1]/ratio 

        cropped = frame[0:int(height), 0:int(width)]

        return cv2.resize(cropped, self.size)
    
live = LiveFeed((1280,720))

#Create an instance of tkinter frame
win = tk.Tk()
win.geometry("1280x720")

frame = live.showFrame()

im = Image.fromarray(frame)
imgtk = ImageTk.PhotoImage(image=im)

feed = tk.Label(win, image= imgtk)
feed.pack()

while True:
    frame = live.showFrame()

    im = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=im)

    #Create a Label to display the image
    feed.configure(image= imgtk)
    win.update()