from Mapping_for_Tkinter import Mapping_for_Tkinter #imports mapping for tkinter class
from tkinter import * #imports tkinter module
import math #imports math module
import time #imports time module

variables=[] #creates empty variables list
variables=(input("Enter v,theta(0,90),strength (return for default 70,60,0.75): ")).split()
if variables==[]: #if no user input is given
    variables=[70,(-1)*(math.radians(60)),.75] #sets default values to list
else:
    variables=[float(variables[0]),(-1)*(math.radians(float(variables[1]))),float(variables[2])] #creates variables list with user inputs
m=Mapping_for_Tkinter(0.0,1200.0,0.0,400.0,1200) #creates class instance 
window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()
ball=canvas.create_oval(-3.5,m.get_height()-3.5,4.5,m.get_height()+4.5,fill="blue") #creates ball of radius 4 in bottom left corner of canvas
x,y,t,rebounds=0,0,0,0 #sets x and y positions, time, and rebounds to 0
firstx,firsty=x,y #sets the first bounce x and y coordinates to 0
running=True #sets running variable for the while loop to true
totaltime=4.4 #creates total time variable
while running: #while loop for when running variable is true
    t+=.1 #adds .1 to time variable
    totaltime+=.1 #adds .1 to totaltime variable
    coords=canvas.coords(ball) #gets coordinates of ball
    trailcoords=[coords[0]+3,coords[1]+3,coords[2]-3,coords[3]-3] #creates coordinates for trail
    canvas.create_oval(trailcoords,fill="black") #creates dots that plot the trajectory of the ball
    xinit,yinit,=x,y #sets initial x and y coordinates for position of the ball
    if coords[1]>=(m.get_height()-4): #if ball rebounds off bottom
        if rebounds>0: #if rebounds is more than 0 (to negate the initial launch of ball)
             variables[0]=variables[0]*variables[2] #changes the angle to rbounding angle
        rebounds+=1 #adds 1 to rebounds
        firstx=x #sets initial position of x at time of rebound
        xinit=x #sets previous x coordinate for moving
        yinit=0 #sets previous y coordinate for moving
        t=.1 #sets time back to .1
    x=firstx+(variables[0]*(math.cos(variables[1])*t)) #gets new x position for moving
    y=(variables[0]*(math.sin(variables[1])*t))+((9.8/2)*(t)**2) #gets new y position for moving
    canvas.move(ball,x-xinit,y-yinit) #moves ball from previous x and y positions to new positions
    window.update() #updates window
    time.sleep(.01) #delays loop .01 seconds
    if variables[0]<.01 or coords[0]>=(m.get_width()-4): #if the ball hits right wall or the speed is below .01 
        running=False #stops loop
canvas.itemconfig(ball,fill="red") #after loop ball turns red
print("Total number of rebounds is: %s"%(rebounds-1)) #displays number of rebounds
print("Total time is: %ss"%(totaltime)) #displays total real time
