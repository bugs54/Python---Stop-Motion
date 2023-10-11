import tkinter as tk
import cv2, time
from PIL import Image, ImageTk
import numpy as np

"""
I want to use multiple windows for the differant functions of the program.

In dev order...
1. Livefeed
2. Capture
3. Timeline
4. Settings
5. File Management
"""

"""
This is the live feed class.
It's used to display what needs to be in the live feed window.

 - I need to add onion skin function to it.
"""
class LiveFeed:
    def __init__(self, size):
        self.size = size
        self.cam = 0 #Which Camera is being used
        self.vid = cv2.VideoCapture(self.cam)
        self.win = tk.Tk()
        self.win.geometry(str(self.size[0]) + "x" + str(self.size[1]))
        self.label = tk.Label(self.win)
        self.label.pack()
    
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
    
    def shownFrame(self):
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
    
    def updateWin(self):
        frame = self.shownFrame()
        
        im = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=im)

        #Create a Label to display the image
        self.label.configure(image= imgtk)
        self.win.update()

    def playBack(self, frames, fps, sinceStart):
        frame = int(fps/sinceStart)

        if frame >= len(frames):
            return False
        im = Image.fromarray(frames[frame])
        imgtk = ImageTk.PhotoImage(image=im)

        #Create a Label to display the image
        self.label.configure(image= imgtk)
        self.win.update()

        return True

if __name__ == "__main__":
    live = LiveFeed((1280,720))

    print(time.time())
    while True:
        live.updateWin()