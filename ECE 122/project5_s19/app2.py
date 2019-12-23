#Project 5 done by Kyle Economou and Ethan LaFleur
import numpy as np #imports numpy module
import matplotlib.pyplot as plt #imports matplot

np.random.seed(7) #sets random seed
n=100000 #sets n
point1=[] #generates empty lists for points of triangle
point2=[]
point3=[]
point1=(input("Enter (x,y) of point-1, default is (0.5,0.5): ")).split() #asks user to input points on triangle
point2=(input("Enter (x,y) of point-2, default is (3,2.5): ")).split()
point3=(input("Enter (x,y) of point-3, default is (1,3): ")).split()
if point1==[]: #if nothing is inputted for point vertices then they are set to default values
    x1,y1=.5,.5
else:
    x1,y1=float(point1[0]),float(point1[1])
if point2==[]:
    x2,y2=3,2.5
else:
    x2,y2=float(point2[0]),float(point2[1])
if  point3==[]:
    x3,y3=1,3
else:
    x3,y3=float(point3[0]),float(point3[1])
xmin,xmax,ymin,ymax=min(x1,x2,x3),max(x1,x2,x3),min(y1,y2,y3),max(y1,y2,y3) #finds xmin xmax ymin ymax
omega=(xmax-xmin)*(ymax-ymin) #finds omega
flist=[] #initializes fsum and flist
fsum=0
iarray=np.array(np.linspace(0,99999,n)) #sets array of values 0-999999
iarray=iarray.astype(int) #makes array integers
areaarray=np.array(np.linspace(0,0,n)) #sets empty array for areas
xarray=np.array(np.random.uniform(xmin,xmax,n)) #generates one  million random points for x and y in arrays
yarray=np.array(np.random.uniform(ymin,ymax,n))
for i in range(n): #for loop to calculate areas of triangle
    A=np.matrix([[x1,x2,x3],[y1,y2,y3],[1,1,1]]) #create matrices to solve for a,b, and c
    B=np.matrix([[xarray[i]],[yarray[i]],[1]])
    Ainv=np.linalg.inv(A) #finds inverse  of matrix A
    X=Ainv*B #mutiplies matrix B with the inverse of matrix A to give us the values of a,b, and c for every i
    a1=float(X[0]) #floats the values of a,b, and c
    a2=float(X[1])
    a3=float(X[2])
    if a1>0 and a2>0 and a3>0: #if a1 a2 and a3 are positive, point is inside circle
        flist.append(1) #appends 1 to flist
    else:
        flist.append(0) #appends 0 to flist
    fsum+=float(flist[i]) #adds corresponding value of f to current sum of f's
    area=(omega/(i+1))*fsum #approximates area
    areaarray[i]=area #writes area in the area of area values
    if i+1==1: #displays approximation of area at specific number of samples
        print("Using 1 samples, area of triangle is ",area)
    elif i+1==10:
        print("Using 10 samples, area of triangle is ",area)
    elif i+1==100:
        print("Using 100 samples, area of triangle is ",area)
    elif i+1==1000:
        print("Using 1000 samples, area of triangle is ",area)
    elif i+1==10000:
        print("Using 10000 samples, area of triangle is %.2f"%(area))
    elif i+1==100000:
        print("Using 100000 samples, area of triangle is %.5f"%(area))
plt.xlim(0,100000) #sets length of axes
plt.ylim(0-.1,max(areaarray)+.1) 
plt.xscale("symlog") #sets scale of x-axis
plt.xlabel("#samples") #labels axes
plt.ylabel("area")
plt.plot(iarray[0:],areaarray[0:],"-b") #plots line  graph
plt.show() #shows plot
xplt1,yplt1=np.array([x1,x2]),np.array([y1,y2]) #puts points of triangle into arrays
xplt2,yplt2=np.array([x3,x2]),np.array([y3,y2])
xplt3,yplt3=np.array([x1,x3]),np.array([y1,y3])
plt.subplot(2,2,1) #creates subplot and puts this plot in top left
plt.xlim(xmin-.1,xmax+.1) #sets how long the axes are
plt.ylim(ymin-.1,ymax+.1)
plt.xticks([]) #take away tick marks on axes
plt.yticks([])
plt.plot(xplt1[0:],yplt1[0:],"-b") #plots three lines of triangle
plt.plot(xplt2[0:],yplt2[0:],"-b")
plt.plot(xplt3[0:],yplt3[0:],"-b")
running=True #sets runninng, inside, and j variables
inside=0
j=0
while running: #plots points until 10 are inside
    if flist[j]==1: #if point is inside
        inside+=1 #adds 1 to number inside
        plt.plot(xarray[j],yarray[j],"o",color="orange",markersize=3) #plots points
        plt.title("m=%s, area=%.3f"%(inside,areaarray[j])) #puts title on plot
    if inside==10: #stops loop
        running=False
    j+=1 #adds 1 to j (total number of samples checked)
plt.subplot(2,2,2) #creates subplot and puts this plot in top right
plt.xlim(xmin-.1,xmax+.1) #sets how long the axes are
plt.ylim(ymin-.1,ymax+.1)
plt.xticks([]) #take away tick marks on axes
plt.yticks([])
plt.plot(xplt1[0:],yplt1[0:],"-b") #plots three lines of triangle
plt.plot(xplt2[0:],yplt2[0:],"-b")
plt.plot(xplt3[0:],yplt3[0:],"-b")
running=True
inside=0
j=0
while running: #plots points until 100 inside
    if flist[j]==1: #if point is inside
        inside+=1 #adds 1 to total points inside
        plt.plot(xarray[j],yarray[j],"o",color="orange",markersize=3) #plots points
        plt.title("m=%s, area=%.3f"%(inside,areaarray[j])) #puts title on plot
    if inside==100: #stops loop
        running=False
    j+=1 #adds 1 to j
plt.subplot(2,2,3) #creates subplot and puts this plot in bottom left
plt.xlim(xmin-.1,xmax+.1) #sets how long the axes are
plt.ylim(ymin-.1,ymax+.1)
plt.xticks([]) #take away tick marks on axes
plt.yticks([])
plt.plot(xplt1[0:],yplt1[0:],"-b") #plots three lines of triangle
plt.plot(xplt2[0:],yplt2[0:],"-b")
plt.plot(xplt3[0:],yplt3[0:],"-b")
running=True
inside=0
j=0
while running: #plots 1000 points inside
    if flist[j]==1: #if point is inside
        inside+=1 #adds 1 to inside
        plt.plot(xarray[j],yarray[j],"o",color="orange",markersize=3) #plots points
        plt.title("m=%s, area=%.3f"%(inside,areaarray[j])) #puts title on plot
    if inside==1000: #stops loop
        running=False
    j+=1 #adds 1 to j
plt.subplot(2,2,4) #creates subplot and puts this plot in bottom right
plt.xlim(xmin-.1,xmax+.1) #sets how long the axes are
plt.ylim(ymin-.1,ymax+.1)
plt.xticks([]) #take away tick marks on axes
plt.yticks([])
plt.plot(xplt1[0:],yplt1[0:],"-b") #plots three lines of triangle
plt.plot(xplt2[0:],yplt2[0:],"-b")
plt.plot(xplt3[0:],yplt3[0:],"-b")
running=True
inside=0
j=0
while running: #plots points until 10,000 are inside
    if flist[j]==1: #if point is inside 
        inside+=1 #adds 1 to inside
        plt.plot(xarray[j],yarray[j],"o",color="orange",markersize=3) #plots points
        plt.title("m=%s, area=%.3f"%(inside,areaarray[j])) #puts title on plot
    if inside==10000: #stops loop
        running=False
    j+=1 #adds 1 to j variable
plt.show() #shows plot