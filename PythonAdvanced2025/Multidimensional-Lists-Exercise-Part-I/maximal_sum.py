# rows, columns = [int(el) for el in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     row_data = [int(el) for el in input().split()]
#     matrix.append(row_data)
#
# max_sum = -9999999999
#
# submatrix = []
#
# for row_index in range(len(matrix) - 2):
#     for col_index in range(len(matrix[row_index]) - 2):
#         top_left = matrix[row_index][col_index]
#         top_center = matrix[row_index][col_index + 1]
#         top_right = matrix[row_index][col_index + 2]
#         middle_left = matrix[row_index + 1][col_index]
#         middle_center = matrix[row_index + 1][col_index + 1]
#         middle_right = matrix[row_index + 1][col_index + 2]
#         bottom_left = matrix[row_index + 2][col_index]
#         bottom_center = matrix[row_index + 2][col_index + 1]
#         bottom_right = matrix[row_index + 2][col_index + 2]
#
#         current_sum = (top_left + top_center + top_right + middle_left + middle_center + middle_right
#                        + bottom_left + bottom_center + bottom_right)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#
#             submatrix = [
#                 [top_left, top_center, top_right],
#                 [middle_left, middle_center, middle_right],
#                 [bottom_left, bottom_center, bottom_right]
#             ]
#
#
# print(f"Sum = {max_sum}")
# print(*submatrix[0])
# print(*submatrix[1])
# print(*submatrix[2])

rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = -float("inf")
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col


print(f"Sum = {max_sum}")

submatrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]

for row in submatrix:
    print(*row)