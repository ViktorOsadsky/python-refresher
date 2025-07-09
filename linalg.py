import numpy as np

a = np.array([1, 2, 3])
print(f"Vector a: {a}")

b = np.array([4, 5, 6])
print(f"Vector b: {b}")

# Addition of vectors
sum_vector = a + b
print(f"Sum of vectors a and b: {sum_vector}")

# Subtraction of vectors
diff_vector = a - b
print(f"Difference of vectors a and b: {diff_vector}")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Addition of matrices
sum_matrix = A + B
print(f"Sum of matrices A and B: {sum_matrix}")

# Subtraction of matrices
diff_matrix = A - B
print(f"Difference of matrices A and B: {diff_matrix}")

dot_product = np.dot(a, b)
print(f"Dot product of vectors a and b: {dot_product}")

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
product_matrix = np.dot(A, B)
print(f"Product of matrices A and B: {product_matrix}")

a = np.array([1, 1, 2])
magnitude = np.linalg.norm(a)
print(f"Magnitude of vector a: {magnitude}")

A = np.array([[1, 2], [3, 4]])
transpose_matrix = A.T
print(f"Transpose of matrix A: {transpose_matrix}")
