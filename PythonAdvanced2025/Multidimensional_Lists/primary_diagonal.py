rows = int(input())

matrix = []
diagonal_sum = 0

for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if row_index == col_index:
            diagonal_sum += matrix[row_index][col_index]

print(diagonal_sum)

