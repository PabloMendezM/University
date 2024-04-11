#needed libraries
import numpy as np
import random as rd

#1. exercise
rd.seed(1347) #seed for the random number

def Mat(size): #function to create the matrix
    A=np.zeros((size,size))
    
    for i in range(size): #fill with random numbers
        for j in range(size):
            A[i,j]=rd.uniform(-5,5)
    return A

A=Mat(6)

#2. exercise
print(np.max(A))
print(np.argmax(A))
 
#!!!!!! always the same values

#3. exercise

row=np.max(A,axis=0)
column=np.max(A,axis=1)

mult=np.dot(row,column)
print(mult)

#4. exercise
B=Mat(6)
C=np.matmul(A,B)
D=np.matmul(B,A)
