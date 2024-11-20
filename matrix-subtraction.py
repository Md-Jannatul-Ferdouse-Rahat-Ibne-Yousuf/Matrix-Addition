import numpy as np

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} separated by space: ").split()))
        if len(row) != cols:
            raise ValueError("All rows must have the same number of columns.")
        matrix.append(row)
    
    return np.array(matrix)

def matrix_subtraction():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    return matrix1 - matrix2