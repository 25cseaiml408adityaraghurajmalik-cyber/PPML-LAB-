# Wap for data types and structures in Numpy.

import numpy as np

# NumPy data types
a = np.array([10, 20, 30], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)
c = np.array([True, False, True], dtype=np.bool_)

print("Integer array:", a)
print("Data type:", a.dtype)

print("\nFloat array:", b)
print("Data type:", b.dtype)

print("\nBoolean array:", c)
print("Data type:", c.dtype)


# NumPy data structures
# 1-D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n1-D Array:")
print(arr1)

print("\n2-D Array:")
print(arr2)

print("\n3-D Array:")
print(arr3)

print("\nDimensions:")
print("arr1:", arr1.ndim)
print("arr2:", arr2.ndim)
print("arr3:", arr3.ndim)
