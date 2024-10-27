# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Message ,Text
from tkinter import *
import tkinter.messagebox
import PIL
from PIL import ImageTk
from PIL import Image
import os
import subprocess
import webbrowser

window = tk.Tk()
window.title("")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
 
#window.geometry('1280x720')
#window.configure(background='#3b5999')

bg= ImageTk.PhotoImage(file="./bg2.jpg")
#Create a canvas
canvas= Canvas(window,width= 400, height= 200)
canvas.pack(expand=True, fill= BOTH)
#Add the image in the canvas
canvas.create_image(0,0,image=bg, anchor="nw")

window.wm_attributes("-transparentcolor", 'grey')

window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

        
def awrite(): 
	os.system("python canvay.py")
	exit()
	
def awriterec(): 
	os.system("python vwrtite.py")
	exit()
	
appwr = tk.Button(window, text="Write", command=awrite  ,fg="white"  ,bg="#6699cc"  ,width=20  ,height=2, activebackground = "#99ccff" ,font=('times', 15, ' bold '))
appwr.place(x=1100, y=370)

appwrr = tk.Button(window, text="Write And Rec", command=awriterec  ,fg="white"  ,bg="#6699cc"  ,width=20  ,height=2, activebackground = "#99ccff" ,font=('times', 15, ' bold '))
appwrr.place(x=1100, y=520)

appquit = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="#6699cc"  ,width=20  ,height=2, activebackground = "#99ccff" ,font=('times', 15, ' bold '))
appquit.place(x=1100, y=670)

 
window.mainloop()
