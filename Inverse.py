import numpy as np

# Function 1: Input a matrix as a numpy array
def input_matrix():
    rows = int(input("Enter the size of the square matrix: "))
    print(f"Enter the elements row by row:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

# Function 2: Calculate determinant using recursion
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0, 0]
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    det = 0
    for col in range(n):
        minor = generate_minor(matrix, 0, col)
        det += ((-1) ** col) * matrix[0, col] * determinant(minor)
    return det

# Function 3: Generate a minor matrix
def generate_minor(matrix, row, col):
    return np.array([
        [matrix[i, j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ])

# Function 4: Generate the cofactor matrix
def cofactor_matrix(matrix):
    n = len(matrix)
    cofactor = np.zeros_like(matrix)
    for row in range(n):
        for col in range(n):
            minor = generate_minor(matrix, row, col)
            cofactor[row, col] = ((-1) ** (row + col)) * determinant(minor)
    return cofactor

# Function 5: Generate the adjoint matrix
def adjoint_matrix(matrix):
    cofactor = cofactor_matrix(matrix)
    return cofactor.T

# Function 6: Calculate the inverse matrix
def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible (determinant is zero).")
    adjoint = adjoint_matrix(matrix)
    return adjoint / det

# Main function to execute all operations
def main():
    print("Enter the square matrix:")
    matrix = input_matrix()

    try:
        print("\nStep 1: Determinant Calculation")
        det = determinant(matrix)
        print(f"Determinant: {det}")

        if det == 0:
            print("Matrix is not invertible because the determinant is zero.")
            return

        print("\nStep 2: Cofactor Matrix Generation")
        cofactor = cofactor_matrix(matrix)
        print("Cofactor Matrix:\n", cofactor)

        print("\nStep 3: Adjoint Matrix Calculation")
        adjoint = adjoint_matrix(matrix)
        print("Adjoint Matrix:\n", adjoint)

        print("\nStep 4: Inverse Matrix Calculation")
        inverse = inverse_matrix(matrix)
        print("Inverse Matrix:\n", inverse)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
