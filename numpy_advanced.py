import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape
reshaped = arr.reshape(2, 3)
print("Reshaped Array:\n", reshaped)

# 2D array
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("2D Array:\n", arr2)

# Indexing
print("Element:", arr2[0][1])

# Random numbers
rand_arr = np.random.randint(1, 50, 5)
print("Random:", rand_arr)

# Math operations
nums = np.array([1, 2, 3])
print("Add:", nums + 10)
print("Multiply:", nums * 2)