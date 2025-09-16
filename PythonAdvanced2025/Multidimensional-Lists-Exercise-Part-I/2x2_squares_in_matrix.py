# rows, columns = [int(el) for el in input().split(" ")]
#
# matrix = []
# count = 0
#
# for _ in range(rows):
#     row_data = [str(el) for el in input().split(" ")]
#     matrix.append(row_data)
#
# for row_index in range(len(matrix) -1):
#     for col_index in range(len(matrix[row_index]) -1):
#         top_left = matrix[row_index][col_index]
#         top_right = matrix[row_index][col_index + 1]
#         bottom_left = matrix[row_index + 1][col_index]
#         bottom_right = matrix[row_index + 1][col_index + 1]
#
#         if top_left == top_right == bottom_left == bottom_right:
#             count +=1
#
# print(count)


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)




