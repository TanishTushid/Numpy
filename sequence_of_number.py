#creating sequences of number in array

"""arange() - like a range func in python , difference
   only they return numpy array
   arange(start,stop,step)
   """
import numpy as np

arr = np.arange(1,10,2)
print(arr)


#creating identities matrix

identity_matrix = np.eye(100)
print("identity matrix")
print(identity_matrix)