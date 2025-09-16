rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

max_sum = -999999999
sub_matrix = []

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        current_sum = current_element + next_element + element_below + element_diagonal
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [element_below, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

