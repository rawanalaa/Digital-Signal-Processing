from math import radians
import numpy as np
import matplotlib.pyplot as plt
from math import exp

def convloution_disc(signalx,signalh,min,max,xx,xy,hx,hy):
    y=[0]*int(max-min+1)
    a=-1
    for i in range(int(min),int(max),1):
        a+=1
        z=0
        for j in range(int(min),i,1):
            if(i-j<min or i-j>=max): 
                t=0
            else:
                t=signalx[i-j]
            z=z+(signalh[j]*t)
            y[a]=z
        
    x=np.arange(min,max+1,1)
    plotx=plt.subplot2grid((3,3),(0,0),colspan=2)
    ploth=plt.subplot2grid((3,3),(1,0),rowspan=2)
    ploty=plt.subplot2grid((3,3),(0,2),colspan=2 ,rowspan=3)
        
    plotx.stem(xx,xy)
    plotx.set_title('x[n]')

    ploth.stem(hx,hy)
    ploth.set_title('h[n]')

    ploty.stem(x,y)
    ploty.set_title('y[n]')

    plt.tight_layout()
    plt.show()
def hn(signalx,min,max,xx,xy):
    print("Select the h[n]")
    print("1.  h[n] = (n+1)u[n]-(n+1)u[n-5]")
    print("2.  h[n]= δ[n-1] ")
    print("3.  h[n]= (0.99)^n u[n-3] ")
    print("4.  h[n]= 4^n u[2-n] ")
    xt=input()

    if(xt=='1'):
        def h(n2):
            if((n2>=0) and (n2<5)): return (n2+1)
            else : return 0

        n2 = np.arange( min,max,1) 
        h2=[]
        for i in range(len(n2)):
           h2.append(h(n2[i]))
        signalh=dict(zip(n2,h2))
    elif(xt=='2'):
        def h(n2):
            if (n2==1): return 1
            else : return 0

        n2 = np.arange( min,max,1) 
        h2=[]
        for i in range(len(n2)):
           h2.append(h(n2[i]))
        signalh=dict(zip(n2,h2))
    elif(xt=='3'):
        def h(n2):
            if(n2>=3): return pow(0.99,n2)
            else : return 0
        n2 = np.arange(min,max,1)  #range of values used for x (start,end,step)
        h2=[]
        for i in range(len(n2)):
           h2.append(h(n2[i]))
        signalh=dict(zip(n2,h2))
    elif(xt=='4'):
        def h(n2):
            if(n2<3): return pow(4,n2)
            else : return 0
        n2 = np.arange(min,max,1)  #range of values used for x (start,end,step)
        h2=[]
        for i in range(len(n2)):
           h2.append(h(n2[i]))
        signalh=dict(zip(n2,h2))
    else:
        print("Invalid Input !")

    convloution_disc(signalx,signalh,min,max,xx,xy,n2,h2)
def unitstep():
    #u[n]=u[n+z]  1->n>=0
    z=float(input("Enter time shifting factor: "))
    ampscale= (input("Enter the amplitdue scaling factor: "))
    ybound= (1*ampscale)
    #exp= float(input("Enter the "))
    n=np.arange(-z-10,z+10,1)
    y=np.piecewise(n,[(n>=-z),(n<-z)],[ybound,0])
    signal=dict(zip(n,y))
    hn(signal,-z-10,z+10,n,y)
def unitrectangular():
    a=float(input("Enter the least value  "))
    b=float(input("Enter the highest value  "))
    time_s=float(input("Enter time shifting  factor  "))
    time_e =float(input("Enter time expanding factor  "))
    least_b=((a)/time_e)-time_s  
    most_b=((b)/time_e)-time_s 
    ampscale= (input("Enter the amplitdue scaling factor: "))
    ybound= (1*ampscale)
    n =np.arange( least_b-10,most_b+10,1)  
    y=np.piecewise(n,[((n>=a)&(n<b)),((n<a)|(n>=b))],[ybound,0])
    signal=dict(zip(n,y))
    hn(signal,-least_b-10,most_b+10,n,y)
def unitimpulse():
    a= float (input("Enter the shifting factor: "))
    ampscale= (input("Enter the amplitdue scaling factor: "))
    ybound= (1*ampscale)
    n = np.arange( -a-15,a+15,1)  
    y=np.piecewise(n,[n==-a,n!=-a ],[ybound,0])
    signal=dict(zip(n,y))
    hn(signal,-a-10,a+15,n,y)
def discrete():
    print("Enter the number of the selected input signal x[n]")
    print("1- Unit Step Pulse ")
    print("2-Unit Recatngular Pulse ") 
    print("3-Unit Impulse Pulse ")
    xt=input()
    if(xt=='1'):
        unitstep()
    elif (xt=='2'):
        unitrectangular()
    elif (xt=='3'):
        unitimpulse()
    else:
        print("Invalid Input !")
def convloution_cont(t1,x1,t2,h2):
    n= len(x1)+len(h2)-1
    y=[0]*n
    for i in range(n):
     for j in range (len(h2)):
         if(i-j<0 or i-j>=len(x1)):
             t=0
         else :
            t=x1[i-j]
         y[i]=y[i]+(h2[j]*t)

    plotx=plt.subplot2grid((3,3),(0,0),colspan=2)
    ploth=plt.subplot2grid((3,3),(1,0),rowspan=2)
    ploty=plt.subplot2grid((3,3),(0,2),colspan=2 ,rowspan=3)
        
    plotx.plot(t1,x1)
    plotx.set_title('x(t)')

    ploth.plot(t2,h2)
    ploth.set_title('h(t)')

    ploty.plot(y)
    ploty.set_title('y(t)')

    plt.tight_layout()
    plt.show()
def ht(t1,x1,min,max):
    print('\n'+"Choose h(t)")
    print("1.  h(t)= exp(-4t) u(t) ")
    print("2.  h(t) = u(t-3) ")
    print("3.  h(t) = exp(2t)")
    print("4.  h(t) = texp(-t) u(t)")
    xt=input()
    if(xt=='1'):
        def h(t2):
            if((t2>=0)): return exp(-4*t2)
            else : return 0

        t2 = np.arange(min,max,0.01)  #range of values used for x (start,end,step)
        h2=[]

        for i in range(len(t2)):
           h2.append(h(t2[i]))

    elif (xt=='2'):
         def h(t2):
            if((t2>=3)): return 1
            else : return 0

         t2 = np.arange(min,max,0.01)  #range of values used for x (start,end,step)
         h2=[]

         for i in range(len(t2)):
           h2.append(h(t2[i]))  
         
    elif (xt=='3'):
         t2=np.arange(min,max,0.01)
         h2=np.exp(2*t2)
      
    elif (xt=='4'):
         def h(t2):
            if((t2>=0)): return t2*exp(-t2)
            else : return 0

         t2 = np.arange( min,max,0.1)  #range of values used for x (start,end,step)
         h2=[]

         for i in range(len(t2)):
           h2.append(h(t2[i])) 

    else:
        print("Invalid Input !")

    convloution_cont(t1,x1,t2,h2)
def  rectangular() : #rect(t)=rect(t-1.5) 

    t1 = np.arange( -10,10,0.01)  #range of values used for x (start,end,step)
    x1=np.piecewise(t1,[((t1>1)&(t1<2)),((t1<1)|(t1>=2))],[1,0])
    ht(t1,x1,-10,10)
def  sin() :
    
    t1=np.arange(0,15,0.01)
    x1=np.sin(t1)
    ht(t1,x1,0,15)
def  step() :
    #u(t)=u(t+n)   t>n->1 , o.w->0
    t1= np.arange( 0,10,0.01)  
    x1=np.piecewise(t1,[(t1>=1),(t1<1)],[1,0])
    ht(t1,x1,0,10)
def continous():
    
    print("Enter the number of the selected input signal x(t)")
    print("1- Rectangular Function : x(t)=rect(t-1.5) ")
    print("2-Sine Function : sin(t)") 
    print("3-Unit Step Function : u(t-1)")
    xt=input()
    if(xt=='1'):
        rectangular()
    elif (xt=='2'):
        sin()
    elif (xt=='3'):
        step()
    else:
        print("Invalid Input !")
def fil_ter():
    print("Enter the number of the selected input signal x[n]")
    print("1- Unit Step Pulse ")
    print("2-Unit Recatngular Pulse ") 
    print("3-Unit Impulse Pulse ")
    print("4- x[n]=u[n-2]-u[n-6]")
    xt=input() 
    if(xt == '1'):
      z=float(input("Enter time shifting factor: "))
      ampscale= (input("Enter the amplitdue scaling factor: "))
      ybound= (1*ampscale)
      n1=np.arange(-z-10,z+10,1)
      y1=np.piecewise(n1,[(n1>=-z),(n1<-z)],[ybound,0])
      signalx=dict(zip(n1,y1))
    elif(xt == '2'):
        a=float(input("Enter the least value  "))
        b=float(input("Enter the highest value  "))
        time_s=float(input("Enter time shifting  factor  "))
        time_e =float(input("Enter time expanding factor  "))
        least_b=((a)/time_e)-time_s  
        most_b=((b)/time_e)-time_s 
        ampscale= (input("Enter the amplitdue scaling factor: "))
        ybound= (1*ampscale)
        n1 =np.arange( least_b-10,most_b+11,1)  
        y1=np.piecewise(n1,[((n1>=a)&(n1<b)),((n1<a)|(n1>=b))],[ybound,0])
        signalx=dict(zip(n1,y1))
    elif(xt== '3'):
        a= float (input("Enter the shifting factor: "))
        ampscale= (input("Enter the amplitdue scaling factor: "))
        ybound= (1*ampscale)
        n1 = np.arange( -1*a-10,a+10,1)  
        y1=np.piecewise(n1,[n1==-a,n1!=-a ],[ybound,0])
        signalx=dict(zip(n1,y1))
    elif(xt== '4'):
        def h(n1):
            if (n1>=2)and(n1<6): return 1
            else : return 0
        n1 = np.arange( -10,10,1) 
        y1=[]
        for i in range(len(n1)):
           y1.append(h(n1[i]))

        signalx=dict(zip(n1,y1))

    print("Enter the number of filter type")
    print("1- low pass filter ")
    print("2- high pass filter ") 
    print("3- bandpass filter ")
    t=input()
    if (t=='1'):
        b=float(input("set the cuttoff frequency: "))
        def h(n):
            if (n>=-b) and (n<=b): return 1
            else : return 0
        n = np.arange( -3,3,1)
        y=[]
        for i in range(len(n)):
           y.append(h(n[i]))
       
        signalf=dict(zip(n,y))
        #hn(signal,-np.pi-10,-1*np.pi+10,n,y)

    elif (t=='2'):
        b=float(input("set the cuttoff frequency: "))
        def h(n):
            if (n<=-b) or (n>=b): return 1
            else : return 0
        n = np.arange( -3,3,1)
        y=[]
        for i in range(len(n)):
           y.append(h(n[i]))

        signalf=dict(zip(n,y))
        #hn(signal,-np.pi-10,-1*np.pi+10,n,y)

    elif (t=='3'): 
        b1=float(input("set upper limit: "))
        b2=float(input("set the lower limit  "))
        def h(n):
            if (abs(n)<=b1) and (abs(n)>=b2): return 1
            else : return 0
        n = np.arange( -3,3,1)
        y=[]
        for i in range(len(n)):
           y.append(h(n[i]))
        signalf=dict(zip(n,y))
        #hn(signal,-np.pi-10,-1*np.pi+10,n,y)
    else: 
        print ("invalid input!!")

    convloution_disc(signalx,signalf,-3,3,n1,y1,n,y)
def main():
    print("Enter the number of the selected type of signal ")
    print("1- Continous ")
    print("2- Discrete ") 
    print("3- Filter")
    
    xt=input()
    if(xt=='1'):
        continous()
    elif (xt=='2'):
        discrete()
    elif (xt=='3'):
        fil_ter()
    else:
        print("Invalid Input !")


main()




