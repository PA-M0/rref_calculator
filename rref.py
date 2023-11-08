import numpy as np



# Swap the current row with the row containing the pivot
def interchange(matrix, first_row_index, second_row_index):
    matrix[first_row_index], matrix[second_row_index] = matrix[second_row_index], matrix[first_row_index]
#find pivot
def find_pivot(pivot_row, num_row, matrixx,col):
    while pivot_row < num_row and matrixx[pivot_row][col] == 0:
        pivot_row += 1
    return pivot_row
# Make the pivot element 1
def divide_rows_by_their_pivot_enties(matrixx, pivot_element, row):
    matrixx[row] = [entry / pivot_element for entry in matrixx[row]]

def subtract_scaled_pivot_row_from_rows_below(matrixx, pivot_row, pivot_column):
    num_rows = len(matrixx)

    for i in range(pivot_row + 1, num_rows):
        factor = matrixx[i][pivot_column]
        matrixx[i] = [entry - factor * matrixx[pivot_row][idx] for idx, entry in enumerate(matrixx[i])]
    return matrixx

def subtract_scaled_pivot_row_from_rows_above(matrixx, pivot_row, pivot_column):
    for i in range(pivot_row):
        factor = matrixx[i][pivot_column]
        matrixx[i] = [entry - factor * matrixx[pivot_row][idx] for idx, entry in enumerate(matrixx[i])]
    return matrixx

  

def reduced_echelon_form(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    row, col = 0, 0

    while row < num_rows and col < num_cols - 1:
        # Find the leftmost non-zero entry in the current column
        pivot_row = row
        pivot_row = find_pivot(pivot_row, num_rows, matrix, col)
       
     
      

        if pivot_row < num_rows:
            # Swap two row
            interchange(matrix, pivot_row, row)
            
            # Make the pivot element 1
            pivot_element = matrix[row][col]
            divide_rows_by_their_pivot_enties(matrix, pivot_element, row)
           

            # Eliminate all non-zero elements below and above the pivot
            for i in range(num_rows):
                if i != row:
                    factor = matrix[i][col]
                    matrix[i] = [entry - factor * matrix[row][idx] for idx, entry in enumerate(matrix[i])] 
            if augmented_matrix[pivot_row][col] != 0:
                subtract_scaled_pivot_row_from_rows_below(matrix, pivot_row, col)
                subtract_scaled_pivot_row_from_rows_above(matrix, pivot_row, col)
            row += 1
        col += 1

    return matrix


# INPUT:
augmented_matrix =  np.array([
    [1, 1, 0, 0, 0, 800],
    [0, 1, -1, 1, 0, 300],
    [0, 0, 0, 1, 1, 500],
    [1, 0, 0, 0, 1, 600]
], dtype=float)

augmented_matrix = augmented_matrix.tolist()
rref_matrix = reduced_echelon_form(augmented_matrix)
 
print("Reduced Row Echelon Form (RREF) Matrix:")
for row in rref_matrix:
    print(row)



