import numpy as np
import matplotlib.pyplot as plt 
#1. exercise

def c_pol(x,i):
    if i==0: return 1
    if i==1: return x
    return 2*x*c_pol(x, i-1) - c_pol(x, i-2)
    
def cheby(x,N):
    l=np.size(x)
    
    A=np.zeros((l,N+1))
    
    for i in range(l): #fill with random numbers
        for j in range(N+1):
            A[i,j]=c_pol(x[i], j)
    return A


#2. exercise

x=np.linspace(-1,1,100)

A=cheby(x,4)
for i in range(5):
    plt.plot(x,A[:,i],label="T_"+str(i))
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Chebyshev polynomials")