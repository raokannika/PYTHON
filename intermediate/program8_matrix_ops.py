# Program 8: Matrix addition and transpose

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Addition
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Matrix Addition:", C)

# Transpose
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("Transpose of A:", T)
