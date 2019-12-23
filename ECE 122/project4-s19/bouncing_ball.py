from Mapping_for_Tkinter import Mapping_for_Tkinter #imports mapping for tkinter class
from tkinter import * #imports tkinter module
import math #imports math module
import time #imports time module

rebounds=0 #instatiates rebounds variable
minmax=[] #sets minmax list to an empty list
minmax=(input("Enter xmin,xmax,ymin,ymax (return for default -300,300,-300,300): ")).split() #gets user inputs for min and max x and y values
if minmax==[]: #if user does not input anything for xmin xmax ymin ymax
    m=Mapping_for_Tkinter(-300,300,-300,300,600) #sets default values to the class instance
else: #if user inputs numbers
    m=Mapping_for_Tkinter(float(minmax[0]),float(minmax[1]),float(minmax[2]),float(minmax[3]),800) #creates class instance with user inputted values
    rebounds+=1
variables=[] #creates empty list for variables
variables=(input("Enter x0,y0,v,theta (return for default 0,0,70,30): ")).split() #asks for user inputs of x0 y0 velocity and theta
if variables==[]: #if list is still empty
    variables=[0,0,70,((-1)*math.radians(30))] #sets list to default values while making the theta value negative for format of tkinter 
else:
    variables=[float(variables[0]),float(variables[1]),float(variables[2]),(-1)*(math.radians(float(variables[3])))] #sets list to user inputs
window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()
ball=canvas.create_oval(m.get_i(variables[0])-3.5,m.get_j(variables[1])-3.5,m.get_i(variables[0])+4.5,m.get_j(variables[1])+4.5,fill="blue") #creates the ball of radius 4 on the canvas
x,y=variables[0],variables[1] #sets x and y variables to the user inputted values or default values
t=0 #sets time to 0
for i in range(1500): #for statement of about 15s
    t+=.1 #adds .1 to time
    coords=canvas.coords(ball) #gets coordinates of ball object
    trailcoords=[coords[0]+3,coords[1]+3,coords[2]-3,coords[3]-3] #sets values for the trail of the ball
    canvas.create_oval(trailcoords,fill="black") #creates dots that follow the trail of the ball
    xinit=x #sets intitial x position of ball
    yinit=y #sets initial y position of the ball 
    if coords[0]>=(m.get_width()-4): #if ball hits right wall
        variables[3]=(math.pi+variables[3])*(-1) #changes theta to correct value after rebound
        rebounds+=1 #adds 1 to rebounds variable
        variables[0]=m.get_x(m.get_width()) #sets initial x position of ball at the time of rebounding
        xinit=m.get_x(m.get_width()) #also sets intitial x position of ball at time of rebounding
        variables[1]=y #sets intitial y position of ball at time of rebound
        yinit=y #also sets initial y position of ball at time of rebound
        t=.1 #sets time back to .1
    elif coords[2]<=4: #if ball hits left wall
        variables[3]=(math.pi+variables[3])*(-1) #changes theta to correct value after rebound
        rebounds+=1 #adds 1 to rebounds variable
        variables[0]=m.get_x(0) #sets initial x position of ball at the time of rebounding
        variables[1]=y #sets intitial y position of ball at time of rebound
        xinit=m.get_x(0) #also sets intitial x position of ball at time of rebounding
        yinit=y #also sets initial y position of ball at time of rebound
        t=.1 #sets time back to .1
    elif coords[3]<=4: #if ball hits top wall
        variables[3]=variables[3]*(-1) #changes theta to correct value after rebound
        rebounds+=1 #adds 1 to rebounds variable
        variables[0]=x #sets initial x position of ball at the time of rebounding
        xinit=x #also sets intitial x position of ball at time of rebounding
        variables[1]=m.get_y(0) #sets intitial y position of ball at time of rebound
        yinit=m.get_y(0) #also sets initial y position of ball at time of rebound
        t=.1 #sets time back to .1
    elif coords[1]>=(m.get_height()-4): #if ball hits bottom wall 
        variables[3]=(-1)*variables[3] #changes theta to correct value after rebound
        rebounds+=1 #adds 1 to rebounds variable
        variables[0]=x #sets initial x position of ball at the time of rebounding
        xinit=x #also sets intitial x position of ball at time of rebounding
        variables[1]=m.get_y(m.get_height()) #sets intitial y position of ball at time of rebound
        yinit=m.get_y(m.get_height()) #also sets initial y position of ball at time of rebound
        t=.1 #sets time back to .1
    x=variables[0]+(variables[2]*(math.cos(variables[3])*t)) #gets new x value for the ball to be moved to
    y=variables[1]+(variables[2]*(math.sin(variables[3])*t)) #gets new y value for the ball to be moved to
    canvas.move(ball,x-xinit,y-yinit) #moves the ball from old x and y postions to new ones
    window.update() #updates the window
    time.sleep(.01) #delays .01 seconds
canvas.itemconfig(ball,fill="red") #once loop is done the ball turns red
print("Total number of rebounds is: %s"%(rebounds)) #displays number of rebounds
