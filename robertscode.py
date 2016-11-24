import time
from random import *
# Get TKinter ready to go
from tkinter import *
window = Tk()
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack(padx=10,pady=10)
# The velocity, or distance moved per time step
# How many directions in a 90degrees angle
vx = randint(0,90)/90 # x velocity
vy = 1-vx # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 800.0
y_max = 600.0
id1=canvas.create_rectangle(0,0,0+10,0+10) #Robot
# Object coordinates
# Wall1
Obx11=350
Oby11=200
Obx12=350+50
Oby12=200+300
id2=canvas.create_rectangle(Obx11, Oby11, Obx12, Oby12, fill='blue')
# Wall2
Obx21=0
Oby21=200
Obx22=350+50
Oby22=200+50
id3=canvas.create_rectangle(Obx21, Oby21, Obx22, Oby22, fill='blue') 
  
# Move robot for 500 timesteps
for t in range(1, 50000):
    x1,y1,x2,y2=canvas.coords(id1)
    Obx11,Oby11,Obx12,Oby12=canvas.coords(id2)
    Obx21,Oby21,Obx22,Oby22=canvas.coords(id3)
    if y2 >= Oby21 and x2>Obx21 and x1<Obx22 and y2<Oby21+10:
        vy = -randint(0,90)/90
        if vx<=0:
            vx=-(1+vy)
        elif vx>=0:
            vx=(1+vy)
        print("Obj top side, x: "+str(vx)+", y: "+str(vy))
    if x2>=Obx21 and y1<=Oby22 and x2<Obx21+10 and y2>=Oby21:
        vx = -randint(0,90)/90
        if vy<=0:
            vy=-(1+vx)
        elif vy>=0:
            vy=(1+vx)
    if y1 <= Oby22 and (x1>Obx21 and x2<Obx22) and y1>Oby22-10:
        vy = randint(0,90)/90
        if vx<=0:
            vx=-(1-vy)
        elif vx>=0:
            vx=(1-vy)
    if x1<=Obx22 and y1<=Oby22 and y2>=Oby21 and x1>Obx22-10:
        vx = randint(0,90)/90
        if vy<=0:
            vy=-(1-vx)
        elif vy>=0:
            vy=(1-vx)
    
    if y2 >= Oby11 and x2>Obx11 and x1<Obx12 and y2<Oby11+10:
        vy = -randint(0,90)/90
        if vx<=0:
            vx=-(1+vy)
        elif vx>=0:
            vx=(1+vy)
        print("Obj top side, x: "+str(vx)+", y: "+str(vy))
    if x2>=Obx11 and y1<=Oby12 and x2<Obx11+10 and y2>=Oby11:
        vx = -randint(0,90)/90
        if vy<=0:
            vy=-(1+vx)
        elif vy>=0:
            vy=(1+vx)
    if y1 <= Oby12 and (x1>Obx11 and x2<Obx12) and y1>Oby12-10:
        vy = randint(0,90)/90
        if vx<=0:
            vx=-(1-vy)
        elif vx>=0:
            vx=(1-vy)
    if x1<=Obx12 and y1<=Oby12 and y2>=Oby11 and x1>Obx12-10:
        vx = randint(0,90)/90
        if vy<=0:
            vy=-(1-vx)
        elif vy>=0:
            vy=(1-vx)
            
    if x2 >= x_max:
        vx = -randint(0,90)/90
        if vy<=0:
            vy=-(1+vx)
        elif vy>=0:
            vy=(1+vx)
        print("max x "+str(vx)+", "+str(vy))
    if y1 <= y_min:
        vy = randint(0,90)/90
        if vx<=0:
            vx=-(1-vy)
        elif vx>=0:
            vx=(1-vy)
        print("min y "+str(vx)+", "+str(vy))
    if y2 >= y_max:
        vy = -randint(0,90)/90
        if vx<=0:
            vx=-(1+vy)
        elif vx>=0:
            vx=(1+vy)
        print("max y "+str(vx)+", "+str(vy))
    if x1 <= x_min:
        vx = randint(0,90)/90
        if vy<=0:
            vy=-(1-vx)
        elif vy>=0:
            vy=(1-vx)
        print("min x "+str(vx)+", "+str(vy))
    # Move robot a fixed amount
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    # the only thing we change, it changes the speed.((seconds from x0 to x1)/x1)
    time.sleep(0.00375)
window.mainloop()
