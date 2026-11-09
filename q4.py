# WAP for dtatistical operations and broadcasting on arrays.

import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

# Statistical Operations
print("\n--- Statistical Operations ---")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# Broadcasting
print("\n--- Broadcasting ---")

# Adding a scalar to every element
result1 = arr + 5
print("Array + 5:", result1)

# Multiplying every element by a scalar
result2 = arr * 2
print("Array * 2:", result2)

# Broadcasting with another array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

result3 = a + b

print("\nArray A:")
print(a)

print("\nArray B:")
print(b)

print("\nA + B using broadcasting:")
print(result3)
