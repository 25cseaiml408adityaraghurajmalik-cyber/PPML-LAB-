# WAP for ndarray object, indexing, and slicing.


import numpy as np

array = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20])

print("Array:", array)

# Indexing
print("Find first index:", array[0])
print("Find third element:", array[2])
print("Find sixth element:", array[5])

# Slicing
print("Print elements from 1-7:", array[0:6])
print("Print elements from 3-8:", array[2:9])
print("Print elements from 3-8:", array[2:9:2])