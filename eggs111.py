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
nreggs=4
eggs=[[0,0]]
colors=['red','yellow','green','blue']
for e in range(1,nreggs+1):
    print("start code")
    globals()["x"+str(e)+"1"]=randint(0,x_max-20)
    globals()["y"+str(e)+"1"]=randint(0,y_max-35)
    if len(eggs)>=1:
        for pos in eggs:
            while math.sqrt((globals()["x"+str(e)+"1"]-pos[0])**2)<20 or math.sqrt((pos[0]-globals()["x"+str(e)+"1"])**2)<20:
                globals()["x"+str(e)+"1"]=randint(0,x_max-20)
                print("while loop x")
            while math.sqrt((globals()["y"+str(e)+"1"]-pos[1])**2)<35 or math.sqrt((pos[1]-globals()["y"+str(e)+"1"])**2)<35:
                globals()["y"+str(e)+"1"]=randint(0,y_max-35)
                print("while loop y")
    globals()["x"+str(e)+"2"]=globals()["x"+str(e)+"1"]+20
    globals()["y"+str(e)+"2"]=globals()["y"+str(e)+"1"]+35
    eggs.append([globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"]])
    globals()["egg"+str(e)]=canvas.create_oval(globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"],globals()["x"+str(e)+"2"],globals()["y"+str(e)+"2"], fill=colors[randint(0,3)], outline='black')
    globals()["x"+str(e)+"1"],globals()["y"+str(e)+"1"],globals()["x"+str(e)+"2"],globals()["y"+str(e)+"2"]=canvas.coords(globals()["egg"+str(e)])
    print("end code")
window.mainloop()
