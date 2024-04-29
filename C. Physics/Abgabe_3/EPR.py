import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

#seeding
rd.seed(3517)

#parameters
T=int(1e3) #time span of an experiment
W=1 #time condition
repetitions=int(1) # rep of the experiment for the statistics
datapoints=25 #amount of data points

#Function that simulates the emission of two particles
def source(M): 
    eta=rd.uniform(0,2*np.pi,M) #random angle, this is the only parameter needed to describe the singlet state
    return eta

def electro_optic_modulator(M,eta,a,a_,b=0,b_=0): #here we use a_ instead of a'
    #random setting of the modulators
    A_1=rd.choice([-1,1],M) 

    #output angles after entering the modulator
    angle_1 = eta - (a*(1+A_1)/2    +   a_*(1-A_1)/2) 
    angle_2 = eta + np.pi/2

    return angle_1,angle_2,A_1

def beamsplitter(M,angle):
    r=rd.uniform(0,1,M)
    r_=rd.uniform(0,1,M)
    t=T*r_*np.sin(2*angle)**4
    return (r<=np.cos(angle)**2)*2 - np.ones(M), t


def Experiment(M=int(1e6),a=np.pi/2,a_=-np.pi/2):
    eta=source(M)

    alpha_1,alpha_2,A_1=electro_optic_modulator(M,eta,a,a_)

    x_1,t_1=beamsplitter(M,alpha_1)
    x_2,t_2=beamsplitter(M,alpha_2)
    
    return x_1,t_1,A_1,x_2,t_2


#processing data
def Compute_coincidence(x_1,t_1,A_1,x_2,t_2):

    pp = np.sum(np.where((x_1 == 1) & (x_2 == 1) & (abs(t_1-t_2) < W) & (A_1 == 1), 1, 0))

    pm = np.sum(np.where((x_1 == 1) & (x_2 == -1) & (abs(t_1-t_2) < W) & (A_1 == 1), 1, 0))

    mp = np.sum(np.where((x_1 == -1) & (x_2 == 1) & (abs(t_1-t_2) < W) & (A_1 == 1), 1, 0))

    mm = np.sum(np.where((x_1 == -1) & (x_2 == -1) & (abs(t_1-t_2) < W) & (A_1 == 1), 1, 0))

    E1=(pp+pm-mp-mm)/(pp+pm+mp+mm)

    E2= (pp+mp-pm-mm)/(pp+pm+mp+mm)

    E12= (pp+mm-pm-mp)/(pp+pm+mp+mm)

    return E1,E2,E12

angles=np.linspace(0,2*np.pi,datapoints)
x=np.linspace(0,2*np.pi)
E1=np.zeros(datapoints)
E2=np.zeros(datapoints)
E12=np.zeros(datapoints)

for i,angle in enumerate(angles):
    for j in range(repetitions):
        x_1,t_1,A_1,x_2,t_2=Experiment(a=angle,a_=angle-np.pi/2)
        m,n,p=Compute_coincidence(x_1,t_1,A_1,x_2,t_2)
        E1[i] +=m/repetitions
        E2[i] +=n/repetitions
        E12[i] +=p/repetitions

plt.figure()
plt.scatter(angles,E1*E2)
plt.plot(x,-np.cos(2*x)*0,color="red")
plt.ylim(-1,1)



plt.figure()
plt.scatter(angles,E12)
plt.plot(x,-np.cos(2*x),color="red")

plt.figure()
plt.scatter(angles,E12+np.cos(2*angles))
plt.plot(x,np.cos(2*x)*0,color="red")