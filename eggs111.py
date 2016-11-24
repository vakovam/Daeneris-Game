from tkinter import *
import time
from random import *
import math
window = Tk()
canvas = Canvas(window,width=800, height=600, bg='white')
canvas.pack()
x_max=800
y_max=600
#Create eggs of different colours
nreggs=4 ##Change the number of eggs on the map.
eggs=[] #List of all egg's x1,y1 as [x1,y1]
colors=['red','yellow','green','blue'] ##Egg Colors
for e in range(1,nreggs+1):
    globals()["x"+str(e)+"1"]=randint(0,x_max-20)
    globals()["y"+str(e)+"1"]=randint(0,y_max-35)
    if len(eggs)>=1:
        for pos in eggs:
            while math.sqrt((globals()["x"+str(e)+"1"]-pos[0])**2)<20 or math.sqrt((pos[0]-globals()["x"+str(e)+"1"])**2)<20:
                globals()["x"+str(e)+"1"]=randint(0,x_max-20)
            while math.sqrt((globals()["y"+str(e)+"1"]-pos[1])**2)<35 or math.sqrt((pos[1]-globals()["y"+str(e)+"1"])**2)<35:
                globals()["y"+str(e)+"1"]=randint(0,y_max-35)
    globals()["x"+str(e)+"2"]=globals()["x"+str(e)+"1"]+20 ##20 is the x size of the egg.
    globals()["y"+str(e)+"2"]=globals()["y"+str(e)+"1"]+35 ##35 is the y size of the egg.
    eggs.append([globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"]])
    globals()["egg"+str(e)]=canvas.create_oval(globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"],globals()["x"+str(e)+"2"],globals()["y"+str(e)+"2"], fill=colors[randint(0,3)], outline='black')

    
    globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"],globals()["x"+str(e)+"2"],globals()["y"+str(e)+"2"]=canvas.coords(globals()["egg"+str(e)])##This one we add in the timesteps loop.
window.mainloop()
