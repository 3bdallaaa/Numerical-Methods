import math

#################################################

def bisection(a,b,error):
    step=0 ; condition=True
    print('\nBisection method\n')
    print(" Iteration |    c   |   f(c)  |     Interval      | Segma")
    while condition:
        c=(a+b)/2 ; step+=1
        if (b-c)>=error:
            if f(c)<0:    
                print('    %.2d     | %0.4f | %0.4f | [%0.4f , %0.4f] | %0.4f'%(step,c,f(c),c,b,b-c))
            else:
                print('    %.2d     | %0.4f |  %0.4f | [%0.4f , %0.4f] | %0.4f'%(step,c,f(c),c,b,b-c))
        else: break

        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    if f(c)<0:    
        print('    %.2d     | %0.4f | %0.4f | [%0.4f , %0.4f] | %0.4f'%(step,c,f(c),c,b,b-c))
    else:
        print('    %.2d     | %0.4f |  %0.4f | [%0.4f , %0.4f] | %0.4f'%(step,c,f(c),c,b,b-c))
    print('\nRequired root is c= %0.4f'%c)
    if f(a)*f(b)>0:
        print('\nTry again\n')

#################################################

def false_position(a,b,max):
    step=x=0 ; condition=True
    print('\nFalse position method\n')
    print(" Iteration |   c    |   f(c)  |    Interval ")

    while condition==True:
        c=b-(f(b)*(b-a)/(f(b)-f(a))) ; step+=1
        
        if (float(c)==float(x)) or (abs(f(c))) ==float(0) or step>max:
            condition=False ; break
        else:
            print('    %.2d     | %0.4f | %0.4f | [%0.4f , %0.4f] '%(step,c,f(c),a,b))
            x=c

        if f(a)*f(c)<0:
            b=c
        else:
            a=c
       
    print('\nRequired root is c= %0.4f'%c)
        
#################################################

def secant(x0,x1,error):
    print('\nSecant Method')
    step=0 ; condition=True
    print(" Iteration |   xi-1  |  f(xi-1) |    xi   |   f(xi)  |   xi+1  | Segma")
    while condition:
        if f(x0)==f(x1):
            print('Divide by zero error') ; break
        x2=x1-(f(x1)*(x1-x0)/(f(x1)-f(x0)))  ; step+=1

        if f(x1)<0:    
            print('    %2d     | %0.4f |  %0.4f |  %0.4f |  %0.4f |  %0.4f | %0.4f'%(step,x0,f(x0),x1,f(x1),x2,abs(x2-x1)))
        else:
            print('    %2d     | %0.4f |  %0.4f |   %0.4f |   %0.4f |  %0.4f | %0.4f'%(step,x0,f(x0),x1,f(x1),x2,abs(x2-x1)))

        x0=x1 ; x1=x2 
        condition=abs(x2-x1)>error
    x2=x1-(f(x1)*(x1-x0)/(f(x1)-f(x0)))
    if f(x1)<0:    
        print('    %2d     | %0.4f |  %0.4f |  %0.4f |  %0.4f |  %0.4f | %0.4f'%(step,x0,f(x0),x1,f(x1),x2,abs(x2-x1)))
    else:
        print('    %2d     | %0.4f |  %0.4f |  %0.4f |   %0.4f |  %0.4f | %0.4f'%(step,x0,f(x0),x1,f(x1),x2,abs(x2-x1)))
    print('\nRequired root is xi+1= %0.4f'%x2)

#################################################

#def f5(x):
#    return x*x*x+x*x-1

#def g5(x):
#    return 1/math.sqrt(1+x)

def FixedPoint(x0,max):
    step=0 ; flag=1 ; condition=True
    print('\nFixed Point\n')
    print(" Iteration |    xi   |   f(xi)  ")
    if abs(g1(x0))<1:
        while condition:
            x1=f1(x0) ; step+=1
            print('    %.2d     | %02.4f | %0.4f '%(step,x1,f1(x1)))
            if step+1>max or x0==x1:
                flag=0 ; break
            condition= x0>x1 or x0<x1 #equivelent lel not equal
            x0=x1
        if flag==1:
            print('\nRequirred root is xi= %0.4f'%x1)
    else:
        print('\nNot convergent\n')

#################################################

def Newton(x):
    step=0 ; condition=True
    print('\nNewton Raphson Method\n')
    print("Iteration |   xi   | f(xi)  | f'(xi) ")

    while condition==True:
        if g(x)==0:
            print('\nDivide by zero error.\n') ; break    
        x1=x-f(x)/g(x) ; step+=1
        if float(x)==float(x1):
            condition=False ; break
        elif abs(f(x)) ==0.0000:
            condition=False ; break
        else:
            print('    %d     | %0.4f | %0.4f | %0.4f '%(step,x,f(x),g(x)))
            x=x1 
    print('\nRequired root is xi= %0.4f'%x1)

#################################################
                                                ######### Main ##########
print('\n Choose a Method from the following:')
choice=-1
while choice<0 or choice>5:
    while choice<0 or choice>5:
        choice=int(input('\n 1.Bisection\n 2.False position\n 3.Secant\n 4.Newton \n 5.Fixed Point\n 0.Exit \n\n choice='))    
    

    if choice == 0:
        print('\nThank you :)\n')    

    else:
        print('\nEnter the equation \n')
        if choice>0 and choice<5:
            z=int(input('coff. of x^4 ='))
            q=int(input('coff. of x^3 ='))
            w=int(input('coff. of x^2 ='))
            e=int(input('coff. of x   ='))
            r=int(input('free coff.   ='))

            def f(x):
                return z*x**4 +q*x**3 + w*x**2 + e*x + r
#                return   x**3-x-1
            def g(x):    #for newton
                return 4*z*x**3 +3*q*x**2 + 2*w*x + e
#                return 3*x**2-1

        elif choice ==5:
            q=int(input('power of x ='))
            w=int(input('coff. of x^%d ='%q))
            e=int(input('coff. of x ='))
            r=int(input('free coff.  ='))

            def f1(x): #for fixed point
                return q*x**w + e*x + r # --->  X= ((e*x+r)/q)**(1/w)
            def g1(x): 
                return (1/w)*(((e*x+r)/q)**((1/w)-1))*((e/q))

        if choice == 1:
            a=float(input(' a= '))
            b=float(input(' b= '))
            error=float(input('Error= '))    
            bisection(a,b,error)
        
        if choice == 2:
            a=float(input(' a= '))
            b=float(input(' b= '))
            max=int(input('Max. steps='))
            if f(a) * f(b)>0:
                print('Try again')
            false_position(a,b,max)

        if choice == 3:
            a=float(input(' x0= '))
            b=float(input(' xi= '))
            error=float(input('Error= '))    
            secant(a,b,error)

        if choice == 4:
            a=float(input(' x0= '))
            Newton(a)

        if choice == 5:
            x0=float(input(' x0= '))
            max=int(input('Max. steps='))
            FixedPoint(x0,max)
        choice=-1