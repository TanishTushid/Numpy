import numpy as np

temperature = np.array([32.5,33.0,25,22.2,20.6])
average = np.mean(temperature)
print(average)

#print(np.mean(temperature))
# no loops use, faster calculation, million on rows are easily handle
# numpy sopport numerical python using arrays
"""feature of numpy
    faster speed 
    less memory
    easy math operations
    imp- ai, data science
    use- data science, ML-AI,stock market , medical research, image processing
"""

"""
list - speed slow        numpy - fast
memory - use more        less
calculation need loops   easy
best with small data     large datasets

"""

python_list = [1,2,3,4,5,6,7,8,9,10]
print(python_list)

numpy_list = np.array([1,2,3,4,5,6,7,8,9,10])
print(numpy_list)