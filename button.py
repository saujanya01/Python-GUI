from tkinter import *

root = Tk()

#FRAMES
topFrame = Frame(root)#initialising for frame on top
bottomFrame = Frame(root)#initialising for frame on bottom
topFrame.pack()#placing of the frames
bottomFrame.pack(side=BOTTOM)#placing the bottomFrame in bottim of the layout

#MAKING WIDGETS
#Button
button1 = Button(topFrame , text = "Button 1" , fg = "red")
button2 = Button(topFrame , text = "Button 2" , fg = "green")
button3 = Button(topFrame , text = "Button 3" , fg = "blue")
button4 = Button(bottomFrame , text = "Button 4" , fg = "violet")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()