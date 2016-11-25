import time
from random import *
# Get TKinter ready to go
from tkinter import *
import math
window = Tk()
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack(padx=10,pady=10)
# The velocity, or distance moved per time step
# How many directions in a 90degrees angle
#vx = randint(0,90)/90 # x velocity
#vy = 1-vx # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 800.0
y_max = 600.0
id1=canvas.create_rectangle(0,0,0+10,0+10) #Robot
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
choseegg = int(input(str(eggs)+"\nWhich egg do you want the robot to go to? "))-1
for t in range(1, 50000):
    x1,y1,x2,y2=canvas.coords(id1)
    for e1 in range(1,nreggs+1):
        globals()["x"+str(e1)+"1"],globals()["y"+str(e1)+"1"],globals()["x"+str(e1)+"2"],globals()["y"+str(e1)+"2"]=canvas.coords(globals()["egg"+str(e1)])
    vy1=1
    vx1=(eggs[choseegg])[0]/(eggs[choseegg])[1]
    vx=vx1/(vy1+vx1)
    vy=vy1/(vy1+vx1)
    # Move robot a fixed amount
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    # Changes the speed((seconds from x1 to x2)/x2)
    time.sleep(0.0166666)
window.mainloop()
