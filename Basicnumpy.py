# importing necessary package
import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"]="2"
import antigravity
# importing necessary packages
import numpy as np
#import gym
int_array1 = np.random.randint(1,10,10)
print(int_array1)
int_array1.reshape(2,5)
int_array2 = np.random.randint(1,20,10)
print(int_array2)
#Concatenate
int_array3 = np.vstack((int_array1,int_array1))
print("vertical concat",int_array3)

int_array4 = np.hstack((int_array1,int_array2))
print("horizontal concat",int_array4)
A_inds = np.where(int_array1==int_array2)
print(A_inds)
m = np.asmatrix(int_array4)
m.shape
print("a=",m[0,0])
print("\n")
print("b=",m[0,:])
print("\n")
print("c=",m[:,0])
print("d=",m[0,8:12])

