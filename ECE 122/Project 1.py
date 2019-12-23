import math

#Task 1 
def my_quad_equation():
   print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c")
   print( )
   a=float(input("Enter a value for a:")) #a is coefficient for x**2, input by user
   b=float(input("Enter a value for b:")) #b is coefficient for x, input by user
   c=float(input("Enter a value for c:")) #c is constant, input by user
   print( )
   print("Equation is: f(x)=%sx**2+%sx+%s"%(a,b,c))
   temp=input("\nPress Enter to continue...") #<-- Waits for user to press enter to continue on in the function

#Task 2	
def evaluate_quad_equation(a,b,c):
   x=float(input("Enter a value for x:")) #x is value for x, input by user
   answer=(a*x**2+b*x+c)
   x=str(x) #x must be a string here
   print("f(%s)=%s"%(x,answer))
   temp=input("\nPress Enter to continue...") 

	
def my_quad_equation():
   print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c")
   print( )
   a=float(input("Enter a value for a:"))
   b=float(input("Enter a value for b:"))
   c=float(input("Enter a value for c:"))
   print( )
   print("Equation is: f(x)=%sx**2+%sx+%s"%(a,b,c))
   temp=input("\nPress Enter to continue...")
   evaluate_quad_equation(a,b,c) #Calls new function

#Task 3	
def evaluate_quad_equation(a,b,c):
   x=float(input("Enter a value for x:"))
   answer=(a*x**2+b*x+c)
   x=str(x)
   print("f(%s)=%s"%(x,answer))
   temp=input("\nPress Enter to continue...")
   extrema=(-b/(2*a)) #extrema is minimum or maximum value
   y=(a*(extrema**2)+b*(extrema)+c) #y is variable that holds value of the function computed with all user inputs
   if a>0:
	   print("f(x) has a minimum at x0=%s with value f(x0)=%s"%(extrema,y))
   elif a<0:
	     print("f(x) has a maximum at x0=%s with value f(x0)=%s"%(extrema,y))
   temp=input("\nPress Enter to continue...")

#Task 4
def compute_discriminant(a,b,c):
   print("Solving for f(x)=0")
   d=(b**2-(4*a*c)) #d is discriminant of function 
   print("Discriminant is %s"%(d))
   if d>0:
           x1=((-b+math.sqrt(d))/(2*a)) #x1 and x2 can only be computed if d>0. They are the roots of the quadratic
           x2=((-b-math.sqrt(d))/(2*a))
           print("Two real solutions: %s and %s"%(x1,x2))
   elif d==0:
              extrema=(-b/(2*a))
              print("One real solution: %s"%(extrema))
   else:
         print("No real solutions")
   print( )
   print("Thanks for using Quadratic solver!, come back soon")

def my_quad_equation():
   print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c")
   print( )
   a=float(input("Enter a value for a:"))
   b=float(input("Enter a value for b:"))
   c=float(input("Enter a value for c:"))
   print( )
   print("Equation is: f(x)=%sx**2+%sx+%s"%(a,b,c))
   temp=input("\nPress Enter to continue...")
   evaluate_quad_equation(a,b,c)
   compute_discriminant(a,b,c)

#Task 5
def my_quad_equation():
   print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c")
   print( )
   a=float(input("Enter a value for a:"))
   b=float(input("Enter a value for b:"))
   c=float(input("Enter a value for c:"))
   print( )
   if a==1 and b!=1: #if else statements are for if the coefficients are 1, and get rid of the unnecessary coeffecient
                     print("Equation is: f(x)=x**2+%sx+%s"%(b,c))
   elif b==1 and a!=1:
                       print("Equation is: f(x)=%sx**2+x+%s"%(a,c))
   elif a==1 and b==1:
                       print("Equation is: f(x)=x**2+x+%s"%(c))
   else:
         print("Equation is: f(x)=%sx**2+%sx+%s"%(a,b,c))
   temp=input("\nPress Enter to continue...")
   evaluate_quad_equation(a,b,c)
   compute_discriminant(a,b,c)

#Task 6
def my_quad_equation():
   print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c")
   print( )
   a=float(input("Enter a value for a:"))
   b=float(input("Enter a value for b:"))
   c=float(input("Enter a value for c:"))
   print( )
   if a<-1 or (a>-1 and a<0): #Code is separated by a values and have specific code for when the coefficients are 1 so they don't show up unnecessarily
      if (b<-1 and c<0) or (b>-1 and b<0 and c<0):
                                              print("Equation is: %sx**2-%sx-%s"%(a,abs(b),abs(c)))
      elif (b<-1 and c>0) or (b>-1 and b<0 and c>0):
                                                print("Equation is: %sx**2-%sx+%s"%(a,abs(b),c))
      elif b==-1 and c<0:
                         print("Eqaution is: %sx**2-x-%s"%(a,abs(c)))
      elif b==-1 and c>0:
                         print("Equation is: %sx**2-x+%s"%(a,c))
      elif b==1 and c<0:
                        print("Eqaution is: %sx**2+x-%s"%(a,abs(c)))
      elif b==1 and c>0:
                        print("Equation is: %sx**2+x+%s"%(a,c))
      elif (b>1 and c<0) or (b>0 and b<1 and c<0):
                                              print("Equation is: %sx**2+%sx-%s"%(a,b,abs(c)))
      elif (b>1 and c>0) or (b>0 and b<1 and c>0):
                                              print("Equation is: %sx**2+%sx+%s"%(a,b,c))
   elif a==-1:
      if (b<-1 and c<0) or (b>-1 and b<0 and c<0):
                                              print("Equation is: -x**2-%sx-%s"%(abs(b),abs(c)))
      elif (b<-1 and c>0) or (b>-1 and b<0 and c>0):
                                                print("Equation is: -x**2-%sx+%s"%(abs(b),c))
      elif b==-1 and c<0:
                         print("Eqaution is: -x**2-x-%s"%(abs(c)))
      elif b==-1 and c>0:
                         print("Equation is: -x**2-x+%s"%(c))
      elif b==1 and c<0:
                        print("Eqaution is: -x**2+x-%s"%(abs(c)))
      elif b==1 and c>0:
                        print("Equation is: -x**2+x+%s"%(c))
      elif (b>1 and c<0) or (b>0 and b<1 and c<0):
                                              print("Equation is: -x**2+%sx-%s"%(b,abs(c)))
      elif (b>1 and c>0) or (b>0 and b<1 and c>0):
                                              print("Equation is: -x**2+%sx+%s"%(b,c))
   elif a==1:
      if (b<-1 and c<0) or (b>-1 and b<0 and c<0):
                                              print("Equation is: x**2-%sx-%s"%(abs(b),abs(c)))
      elif (b<-1 and c>0) or (b>-1 and b<0 and c>0):
                                                print("Equation is: x**2-%sx+%s"%(abs(b),c))
      elif b==-1 and c<0:
                         print("Eqaution is: x**2-x-%s"%(abs(c)))
      elif b==-1 and c>0:
                         print("Equation is: x**2-x+%s"%(c))
      elif b==1 and c<0:
                        print("Eqaution is: x**2+x-%s"%(abs(c)))
      elif b==1 and c>0:
                        print("Equation is: x**2+x+%s"%(c))
      elif (b>1 and c<0) or (b>0 and b<1 and c<0):
                                              print("Equation is: x**2+%sx-%s"%(b,abs(c)))
      elif (b>1 and c>0) or (b>0 and b<1 and c>0):
                                              print("Equation is: x**2+%sx+%s"%(b,c))
   elif a>1 or (a<1 and a>0):
      if (b<-1 and c<0) or (b>-1 and b<0 and c<0):
                                              print("Equation is: %sx**2-%sx-%s"%(a,abs(b),abs(c)))
      elif (b<-1 and c>0) or (b>-1 and b<0 and c>0):
                                                print("Equation is: %sx**2-%sx+%s"%(a,abs(b),c))
      elif b==-1 and c<0:
                         print("Eqaution is: %sx**2-x-%s"%(a,abs(c)))
      elif b==-1 and c>0:
                         print("Equation is: %sx**2-x+%s"%(a,c))
      elif b==1 and c<0:
                        print("Eqaution is: %sx**2+x-%s"%(a,abs(c)))
      elif b==1 and c>0:
                        print("Equation is: %sx**2+x+%s"%(a,c))
      elif (b>1 and c<0) or (b>0 and b<1 and c<0):
                                              print("Equation is: %sx**2+%sx-%s"%(a,b,abs(c)))
      elif (b>1 and c>0) or (b>0 and b<1 and c>0):
                                              print("Equation is: %sx**2+%sx+%s"%(a,b,c))
   temp=input("\nPress Enter to continue...")
   evaluate_quad_equation(a,b,c)
   compute_discriminant(a,b,c)

#Task 7
def factorize_form(a,b,d):
   extrema=(-b/(2*a))
   if d>0:
      x1=((-b+math.sqrt(d))/(2*a))
      x2=((-b-math.sqrt(d))/(2*a))
      if a<-1 or (a>-1 and a<0) or a>1 or (a<1 and a>0): #We use absolute value to deal with the redundancy of +-
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=%s*(x-%s)(x-%s)"%(a,x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=%s*(x-%s)(x+%s)"%(a,x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=%s*(x+%s)(x-%s)"%(a,abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=%s*(x+%s)(x+%s)"%(a,abs(x1),abs(x2)))
      elif a==1:
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=(x-%s)(x-%s)"%(x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=(x-%s)(x+%s)"%(x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=(x+%s)(x-%s)"%(abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=(x+%s)(x+%s)"%(abs(x1),abs(x2)))
      elif a==-1:
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=-(x-%s)(x-%s)"%(x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=-(x-%s)(x+%s)"%(x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=-(x+%s)(x-%s)"%(abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=-(x+%s)(x+%s)"%(abs(x1),abs(x2)))
   elif d==0:
      if a<-1 or (a>-1 and a<0) or a>1 or (a<1 and a>0):
         if extrema>0:
                       print("Factorize form is: f(x)=%s*(x-%s)**2"%(a,extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=%s*(x+%s)**2"%(a,abs(extrema)))
      elif a==1:
         if extrema>0:
                       print("Factorize form is: f(x)=(x-%s)**2"%(extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=(x+%s)**2"%(abs(extrema)))
      elif a==-1:
         if extrema>0:
                       print("Factorize form is: f(x)=-(x-%s)**2"%(extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=-(x+%s)**2"%(abs(extrema)))
   print( )
   print("Thanks for using Quadratic solver!, come back soon")

def compute_discriminant(a,b,c,):
   print("Solving for f(x)=0")
   d=(b**2-(4*a*c))
   print("Discriminant is %s"%(d))
   if d>0:
           x1=((-b+math.sqrt(d))/(2*a))
           x2=((-b-math.sqrt(d))/(2*a))
           print("Two real solutions: %s and %s"%(x1,x2))
   elif d==0:
              extrema=(-b/(2*a))
              print("One real solution: %s"%(extrema))
   else:
         print("No real solutions")
   factorize_form(a,b,d)

#Task 8
def factorize_form(a,b,d):
   extrema=(-b/(2*a))
   if d>0:
      x1=((-b+math.sqrt(d))/(2*a))
      x2=((-b-math.sqrt(d))/(2*a))
      if a<-1 or (a>-1 and a<0) or a>1 or (a<1 and a>0):
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=%s*(x-%s)(x-%s)"%(a,x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=%s*(x-%s)(x+%s)"%(a,x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=%s*(x+%s)(x-%s)"%(a,abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=%s*(x+%s)(x+%s)"%(a,abs(x1),abs(x2)))
      elif a==1:
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=(x-%s)(x-%s)"%(x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=(x-%s)(x+%s)"%(x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=(x+%s)(x-%s)"%(abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=(x+%s)(x+%s)"%(abs(x1),abs(x2)))
      elif a==-1:
         if x1>0 and x2>0:
                           print("Factorize form is: f(x)=-(x-%s)(x-%s)"%(x1,x2))
         elif x1>0 and x2<0:
                             print("Factorize form is: f(x)=-(x-%s)(x+%s)"%(x1,abs(x2)))
         elif x1<0 and x2>0:
                             print("Factorize form is: f(x)=-(x+%s)(x-%s)"%(abs(x1),x2))
         elif x1<0 and x2<0:
                             print("Factorize form is: f(x)=-(x+%s)(x+%s)"%(abs(x1),abs(x2)))
   elif d==0:
      if a<-1 or (a>-1 and a<0) or a>1 or (a<1 and a>0):
         if extrema>0:
                       print("Factorize form is: f(x)=%s*(x-%s)**2"%(a,extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=%s*(x+%s)**2"%(a,abs(extrema)))
      elif a==1:
         if extrema>0:
                       print("Factorize form is: f(x)=(x-%s)**2"%(extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=(x+%s)**2"%(abs(extrema)))
      elif a==-1:
         if extrema>0:
                       print("Factorize form is: f(x)=-(x-%s)**2"%(extrema))
         elif extrema<0:
                         print("Factorize form is: f(x)=-(x+%s)**2"%(abs(extrema)))
   elif d<0:
      complex1=(-b/(2*a))
      complex2=(math.sqrt(abs(d))/(2*a)) #complex1 and 2 are the first and second parts of the complex number
      print("Complex solutions are (%s+%sj) and (%s-%sj)"%(complex1,complex2,complex1,complex2))
   print( )
   print("Thanks for using Quadratic solver!, come back soon")

my_quad_equation()


                             
                           
      

                        
      




	
