# rows = int(input())
#
# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# for _ in range(rows):
#     row_data = [int(el) for el in input().split(" ")]
#     matrix.append(row_data)
#
# for index in range(rows):
#     primary_diagonal.append(matrix[index][index])
#     secondary_diagonal.append(matrix[index][rows - index - 1])
#
# primary_sum = sum(primary_diagonal)
# secondary_sum = sum(secondary_diagonal)
# difference = abs(primary_sum - secondary_sum)
#
# print(difference)

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 -i]for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
