"""
+, -, * , //, **, %
"""
import numpy as np
arr = np.array([210,20,30,40,50])

#operations
print(arr+5)
print(arr-5)
print(arr/2)
print(arr*2)
print(arr//2)
print(arr**2)

#aggregation function
"""
np.sum(), .mean(), .avg(), .max(), .min()  .std(), .var()
"""
array = np.array([10,20,30,40,50,60,70,80,90,100])
print("sum function")
print(np.sum(array))
print("min function")
print(np.min(array))
print("max  function")
print(np.max(array))
print("avg function")
print(np.average(array))
print("std function")
print(np.std(array))
print("var function")
printk