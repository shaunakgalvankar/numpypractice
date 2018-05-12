#this code multiplies two matrices


import numpy as np

a=np.array([[1,1,1],[1,1,1],[1,1,1]])
print("A= ")
print(a)

b=np.array([[2,2,2],[2,2,2],[2,2,2]])
print("B= ")
print(b)

c=a.dot(b)
print("c= ")
print(c)