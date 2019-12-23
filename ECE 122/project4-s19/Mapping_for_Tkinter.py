"""Kyle Economou and Ethan LaFleur"""

from tkinter import * #imports tkinter module

class Mapping_for_Tkinter: #instantiates mapping for tkinter class
    def __init__(self,xmin,xmax,ymin,ymax,width): #instantiates the attributes for class
        self.set_xmin(xmin) #sets the attributes by using the set methods defined in the class
        self.set_xmax(xmax)
        self.set_ymin(ymin)
        self.set_ymax(ymax)
        self.set_width(width)
        self.__set_height(width,xmin,xmax,ymin,ymax)
    def set_xmin(self,xmin): #methods that set the values for the attributes and makes them private
        self.__xmin=xmin
    def set_xmax(self,xmax):
        self.__xmax=xmax
        while self.__xmin>self.__xmax:
            self.__xmin,self.__xmax=input("Your xmax is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: ").split()
            self.__xmin,self.__xmax=float(self.__xmin),float(self.__xmax)
    def set_ymin(self,ymin):
        self.__ymin=ymin
    def set_ymax(self,ymax):
        self.__ymax=ymax
        while self.__ymin>self.__ymax:
            self.__ymin,self.__ymax=input("Your ymax is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split()
            self.__ymin,self.__ymax=float(self.__ymin),float(self.__ymax)
    def set_width(self,width):
        self.__width=width
    def __set_height(self,width,ymax,ymin,xmax,xmin):
        self.__height=self.__width*((self.__ymax-self.__ymin)/(self.__xmax-self.__xmin))
    def get_xmin(self): #Methods that get the private values of the attributes for the class. 
        return self.__xmin
    def get_xmax(self):
        return self.__xmax
    def get_ymin(self):
        return self.__ymin
    def get_ymax(self):
        return self.__ymax
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_x(self,i): #methods that change the i and j values of the tkinter canvas and changes them into the math format of x and y coordinates respectively
        if i==0:
            x=self.__xmin
        elif i>0 and i<(self.__width-1):
            x=(i*(self.__xmax-self.__xmin)/(self.__width-1))-self.__xmax
        elif i==(self.__width) or i==(self.__width-1):
            x=self.__xmax
        return x
    def get_y(self,j):
        if j==0:
            y=self.__ymax
        elif j>0 and j<(self.__height-1):
            y=self.__ymax-((j*(self.__ymax-self.__ymin))/(self.__height-1))
        elif j==(self.__height) or j==(self.__height-1):
            y=self.__ymin
        return y
    def get_i(self,xcord): #methods that change the x and y values in the math format to the i and j values to be used by tkinter
        if xcord==self.__xmin:
            i_cord=0
        elif xcord>self.__xmin and xcord<self.__xmax:
            i_cord=((self.__width-1)*(xcord+self.__xmax))/(self.__xmax-self.__xmin)
        elif xcord==self.__xmax:
            i_cord=self.__width
        return i_cord
    def get_j(self,ycord):
        if ycord==self.__ymin:
            j_cord=self.__height
        elif ycord>self.__ymin and ycord<self.__ymax:
            j_cord=(((-1*ycord)+self.__ymax)*(self.__height-1))/(self.__ymax-self.__ymin)
        elif ycord==self.__ymax:
            j_cord=0
        return j_cord

    def __str__(self): #returns the information about the class in the correct format
        return "Mapping created between x=["+str(self.__xmin)+","+str(self.__xmax)+"] y=["+str(self.__ymin)+","+str(self.__ymax)+"] math => ("+str(int(self.__width))+","+str(int(self.__height))+") tkinter"

def main():
    m=Mapping_for_Tkinter(-5.0,5.0,-5.0,5.0,500) # instantiate mapping
    print(m) # print info about object
    
    window = Tk() # instantiate a tkinter window
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()
    # create rectangle the Tkinter way
    print("Draw rectangle using tkinter coordinates at (100,400) (400,100)")
    canvas.create_rectangle(100,400,400,100,outline="black")
    
    # create circle using the mapping
    print("Draw circle using math coordinates at center (0,0) with radius 3")
    canvas.create_oval(m.get_i(-3.0),m.get_j(-3.0),m.get_i(3.0),m.get_j(3.0),outline="blue")
    
    # create y=x line pixel by pixel using the mapping
    print("Draw line math equation y=x pixel by pixel using the mapping")
    for i in range(m.get_width()):
        x=m.get_x(i) # obtain the x coordinate
        y=x
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="green") 

    
    window.mainloop() # wait until the window is closed


if __name__=="__main__":
    main()
