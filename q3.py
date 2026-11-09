# WAP for numpy array properies and functions.

import numpy as np

# Creating a NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Array:")
print(arr)

# Array Properties
print("\n--- Array Properties ---")
print("Number of dimensions (ndim):", arr.ndim)
print("Shape of array (shape):", arr.shape)
print("Size of array (size):", arr.size)
print("Data type (dtype):", arr.dtype)
print("Item size (itemsize):", arr.itemsize)

# NumPy Functions
print("\n--- NumPy Functions ---")
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Sum of elements:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Square root:")
print(np.sqrt(arr))
print("Transpose:")
print(np.transpose(arr))
