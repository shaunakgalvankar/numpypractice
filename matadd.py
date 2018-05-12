#this is the code to add and subtract two matrices two matrices
import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("A= ")
print(a)

b=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("B= ")
print(b)

c=a+b
d=a-b

print("A+B= " )
print(c)
print("A-B= " )
print(d)