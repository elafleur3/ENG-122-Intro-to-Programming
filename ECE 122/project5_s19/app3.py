import numpy as np

n=input("Newton fractal z**n=1, Enter n (default 3): ")
point=[]
point=(input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35): ")).split()
if n=="":
    n=3
else:
    n=int(n)
if point==[]:
    xmin,xmax,ymin,ymax=-1.35,1.35,-1.35,1.35
else:
    xmin,xmax,ymin,ymax=float(point[0]),float(point[1]),float(point[2]),float(point[3])
print(xmin,xmax,ymin,ymax)
sol=[]
for i in range(n):
    sol.append(np.exp(1j*(2*(np.pi)*(i))/(n)))
    print(sol[i])
x=np.array(np.linspace(xmin+.00011,xmax,1000))
y=np.array(np.linspace(ymin+.00011,ymax,1000))
C=np.zeros((1000,1000),dtype=complex)
for i in range(1000):
    for j in range(1000):
        C[i,j]=x[j]+1j*y[999-i]
for k in range(20):
    nextc=C[0:,0:]-(((C[0:]**n)-1)/(n*(C[0:]**(n-1))))

