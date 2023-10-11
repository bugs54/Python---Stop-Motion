import tkinter as tk

"""
A window to display all the photos that have been taken
"""
class timeline():
    def __init__(self, size, length, gap):
        self.size = size #size of an individual image
        self.length = length #how many images are displayed at a time
        self.gap = gap #gap between images
        self.win.geometry(str((self.size[0]+gap)*length+gap*2) + "x" + str(self.size[1] + gap * 2))
        self.pos = 0 #how far along the timeline the scroll is
        self.scroll = tk.Scrollbar(self.win, orient="horizontal")
        self.scroll.pack()