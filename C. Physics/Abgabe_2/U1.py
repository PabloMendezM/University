import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

#constants for the simulation
N_part=int(1e4)
N_jump=int(1e3)

#seeding
rd.seed(3789)

x_1 = np.zeros(N_part) #Initialization by zero
Var_x=np.zeros(N_jump) #vector of variances of x

#paralel simulation of all particles
for i in range(N_jump):
    x_1 += rd.choice([-1,1], size = N_part) #doing the next step for each particle
    Var_x[i] = np.sum(x_1**2)/N_part-np.sum(x_1)**2/N_part**2 #Particle statistics


#Parameters for the plot
N_plot=np.linspace(1,N_jump,num=N_jump) #x-axis data 
step=int(N_jump/40) #stepping of the data

#Plots 
plt.plot(N_plot[::step],N_plot[::step],color="red")
plt.scatter(N_plot[::step],Var_x[::step])

#Aesthetics of the Plots
plt.grid()
plt.legend(["Analytical result", "Numerical results"])
plt.xlabel("N")
plt.ylabel(r"$\Delta x^2$ ")
plt.savefig("Variance_plot.pdf", dpi=1000)