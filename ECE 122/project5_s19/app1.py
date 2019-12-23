#Project 5 done by Kyle Economou and Ethan LaFleur
import numpy as np #imports numpy module
import matplotlib.pyplot as plt #imports matplot

np.random.seed(7) #sets random seed
flist=[] #initializes flist to empty list
pisum=0 #initializes pisum to 0
piarray=np.array(np.linspace(0,0,1000000)) #initializes array for all values of pi to be written over later
iarray=np.array(np.linspace(0,999999,1000000)) #initializes array for all values of i 
iarray=iarray.astype(int) #changes values in array to ints
n=1000000 #sets n
xlist=np.array(np.random.uniform(-1,1,n)) #generates a million random numbers for x in an array
ylist=np.array(np.random.uniform(-1,1,n)) #generates a million random numbers for y in an array
for i in range(n): #for list for generating approximations of pi
    if ((xlist[i]**2)+(ylist[i]**2))<=1: #determines if point is in circle
        flist.append(1) #adds 1 to flist 
    else:
        flist.append(0) #adds 0 to flist
    pisum+=float(flist[i]) #adds corresponding value of flist to pilist
    pi=(4/(i+1))*pisum #approximates pi
    piarray[i]=pi #adds value of pi to array
    if i+1==1: #prints values of pi for a specific number of samples
        print("Using 1 samples, pi is ",pi)
    elif i+1==10:
        print("Using 10 samples, pi is ",pi)
    elif i+1==100:
        print("Using 100 samples, pi is ",pi)
    elif i+1==1000:
        print("Using 1000 samples, pi is ",pi)
    elif i+1==10000:
        print("Using 10000 samples, pi is ",pi)
    elif i+1==100000:
        print("Using 100000 samples, pi is %.5f"%(pi))
    elif i+1==1000000:
        print("Using 1000000 samples, pi is ",pi)
plt.xlim(0,n) #sets numbers on x and y axes
plt.ylim(0,4)
plt.xscale("symlog") #sets scale of x axis
plt.xlabel("#samples") #sets labels of x and y axes
plt.ylabel("pi")
piarray[0]=2
plt.plot(iarray[0:],piarray[0:],"-b") #plots points from arrays
plt.show() #shows plot
running=True #initializes running and inside variables
inside=0
plt.subplot(2,2,1) #picks the subplot
plt.ylim(-1.1,1.1) #sets values for x and y axes
plt.xlim(-1.5,1.5)
plt.xticks([]) #gets rid of tick marks on graphs
plt.yticks([])
theta = np.arange(360)*2*np.pi/360
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x,y,"b") #plots circle
j=0 #initializing j variable
while running: #while loop for plotting points
    if flist[j]==1: #if point is in circle
        inside+=1 #adds one to inside variable
        plt.title("n=%s, pi=%.3f"%(inside,piarray[j])) #puts title on subplot
        plt.plot(xlist[j],ylist[j],"o",color="orange",markersize=3) #plots points in circle
    if inside==10: #stops loop
        running=False
    j+=1 #adds 1 to j
running=True #initializes running and inside variables
inside=0
plt.subplot(2,2,2) #picks the subplot
plt.ylim(-1.1,1.1) #sets values for x and y axes
plt.xlim(-1.5,1.5)
plt.xticks([]) #gets rid of tick marks on graphs
plt.yticks([])
theta = np.arange(360)*2*np.pi/360
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x,y,"b") #plots circle
j=0 #initializing j variable
while running: #while loop for plotting points
    if flist[j]==1: #if point is in circle
        inside+=1 #adds one to inside variable
        plt.title("n=%s, pi=%.3f"%(inside,piarray[j])) #puts title on subplot
        plt.plot(xlist[j],ylist[j],"o",color="orange",markersize=3) #plots points in circle
    if inside==100: #stops loop
        running=False
    j+=1 #adds 1 to j
running=True #initializes running and inside variables
inside=0
plt.subplot(2,2,3) #picks the subplot
plt.ylim(-1.1,1.1) #sets values for x and y axes
plt.xlim(-1.5,1.5)
plt.xticks([]) #gets rid of tick marks on graphs
plt.yticks([])
theta = np.arange(360)*2*np.pi/360
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x,y,"b") #plots circle
j=0 #initializing j variable
while running: #while loop for plotting points
    if flist[j]==1: #if point is in circle
        inside+=1 #adds one to inside variable
        plt.title("n=%s, pi=%.3f"%(inside,piarray[j])) #puts title on subplot
        plt.plot(xlist[j],ylist[j],"o",color="orange",markersize=3) #plots points in circle
    if inside==1000: #stops loop
        running=False
    j+=1 #adds 1 to j
running=True #initializes running and inside variables
inside=0
plt.subplot(2,2,4) #picks the subplot
plt.ylim(-1.1,1.1) #sets values for x and y axes
plt.xlim(-1.5,1.5)
plt.xticks([]) #gets rid of tick marks on graphs
plt.yticks([])
theta = np.arange(360)*2*np.pi/360
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x,y,"b") #plots circle
j=0 #initializing j variable
while running: #while loop for plotting points
    if flist[j]==1: #if point is in circle
        inside+=1 #adds one to inside variable
        plt.title("n=%s, pi=%.3f"%(inside,piarray[j])) #puts title on subplot
        plt.plot(xlist[j],ylist[j],"o",color="orange",markersize=3) #plots points in circle
    if inside==10000: #stops loop
        running=False
    j+=1 #adds 1 to j
plt.show()
