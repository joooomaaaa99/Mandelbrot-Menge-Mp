
"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 07.02.2017
"""

import math 
import tkinter

xwidth = 500
yheigt = 500

fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge.")
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
w.pack()
#tk.mainloop()


def callback():
    w.get()
    return()

while True:
  w.focus_set()
  xmin = tkinter.Button(fenster, text = "xMin eingeben", width = 10, command = callback)
  xmax = tkinter.Button(fenster, text = "xMax eingeben", width = 10, command = callback)
  ymin = tkinter.Button(fenster, text = "yMin eingeben", width = 10, command = callback)
  ymax = xmax - xmin + ymin
  
  
  
  w.pack()
