import tkinter as tk
from PIL import Image, ImageTk
import cv2, os

"""
A window to display all the photos that have been taken
"""
class timeline():
    def __init__(self, size, length, gap):
        self.size = size #size of an individual image
        self.length = length #how many images are displayed at a time
        self.gap = gap #gap between images
        self.win = tk.Tk()
        self.win.geometry(str((self.size[0]+gap)*length+gap*2) + "x" + str(self.size[1] + gap * 2))
        self.pos = 0 #how far along the timeline the scroll is
        self.scroll = tk.Scrollbar(self.win, orient="horizontal")
        self.scroll.pack()
        self.frames = []
    
    def addFrame(self, frame):
        
        # get the dimensions of the image
        dim = frame.shape

        # crop the size of the image to be the same ratio as our display
        if self.size[0]/dim[1] > self.size[1]/dim[0]:
            ratio = self.size[0]/dim[1]
        else:
            ratio = self.size[1]/dim[0]
            
        # find the height and width of the corrected ratio
        width = self.size[0]/ratio
        height = self.size[1]/ratio 
        
        # resize the frame to fit the size of our display
        cropped = frame[0:int(height), 0:int(width)]

        frame = cv2.resize(cropped, self.size)

        # convert the frame to a tkinter image
        im = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=im)

        # create a new label in frames array for the new frame
        self.frames.insert(0, tk.Label(self.win))

        # place the image in the new label
        self.frames[0].configure(image = imgtk)

    def updateWin(self):
        self.win.update()

if __name__ == "__main__":
    # open 10 images and display them in the timeline
    tl = timeline([128, 72], 5, 10)
    
    path = "C:\\Users\\bugsw\\OneDrive\\Documents\\My Stopmotion Software\\Python---Stop-Motion\\tkinter\\TestImages"
    test_pics = os.listdir(path)

    for i in test_pics:
        tl.addFrame(cv2.imread(path+"\\"+i))

    while 'normal' == tl.win.state():
        tl.updateWin()