from Mapping_for_Tkinter import Mapping_for_Tkinter #imports class from other file
from tkinter import * #imports tkinter module
from math import * #imports math module

formula=input("Enter math formula (using x variable): ") #asks user for equation to be plotted in a string
minmax=[] #makes minmax list empty
minmax=(input("Enter xmin,xmax,ymin,ymax (return for default -5,5,-5,5): ")).split() #asks user for math values for xmin xmax ymin ymax and assigns them to a list
if minmax==[]: #if statement that instantiates the class mapping for tkinter using the default value if user does not input any values
    m=Mapping_for_Tkinter(-5.0,5.0,-5.0,5.0,800)
else: #if user does input values then they are assigned to the class in float format to be used in math later
    m=Mapping_for_Tkinter(float(minmax[0]),float(minmax[1]),float(minmax[2]),float(minmax[3]),800)
window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()
for i in range(m.get_width()): #for statement with width of the canvas
    x=m.get_x(i) #gets x coordinate from the specific pixel in the for loop
    y=eval(formula) #evaluates user inputted function to give y value
    canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="blue") #creates rectangle at the x and y values
    if (m.get_xmin()<0 and m.get_xmax()>0) and (m.get_ymin()<0 and m.get_ymax()>0): #if statement for if the graph crosses x and y axis
        canvas.create_line(m.get_i(0),0,m.get_i(0),m.get_height()) #draws x axis on canvas
        canvas.create_line(0,m.get_j(0),m.get_width(),m.get_j(0)) #draws y axis on canvas
    elif m.get_xmin()<0 and m.get_xmax()>0: #if statement for if function oinly crosses y axis
        canvas.create_line(m.get_i(0),0,m.get_i(0),m.get_height()) #draws y axis
    elif m.get_ymin()<0 and m.get_ymax()>0: #if statement for if function only crosses x axis
        canvas.create_line(0,m.get_j(0),m.get_width(),m.get_j(0)) #draws x axis


