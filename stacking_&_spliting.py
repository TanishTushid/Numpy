"""

# stacking
there are multiple array which we want to combine
vertically, horizontally we do

vstack() row wise
hstack() column wise
"""

import numpy as np 

print("stacking")

arr = np.array([1,2,3,4,5])
print("first array ")
print(arr)

arr_2 = np.array([6,7,8,9,10])
print("second array")
print(arr_2)

print("vertically")
print(np.vstack((arr,arr_2)))   # vertically stack

print("horizontally")
print(np.hstack((arr,arr_2)))   #horizontally stack

print("\n")
"""
spliting

single array divide into multiple parts

np.split  -> divide into equal part
np.hsplit  -> divide into horizontally
np.vsplit  -> divide into vertically

"""
print("************************************************")
print("\n")
print("spliting")

array = np.array([10,20,30,40,50,60,70,80,90,100])
print("array")
print(array)
print("split")
print(np.split(array,2))

array_2 = np.array([[10,20,30,40,50,],[60,70,80,90,100]])
print("2D array")
print(array_2)
print("hsplit")
print(np.hsplit(array_2,5))
print("vsplit")
print(np.vsplit(array_2,2))
