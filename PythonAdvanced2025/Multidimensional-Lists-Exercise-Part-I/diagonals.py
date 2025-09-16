# rows = int(input())
#
# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# for _ in range(rows):
#     row_data = [int(el) for el in input().split(", ")]
#     matrix.append(row_data)
#
# for index in range(rows):
#     primary_diagonal.append(matrix[index][index])
#     secondary_diagonal.append(matrix[index][rows - index - 1])
#
# primary_sum = sum(primary_diagonal)
# secondary_sum = sum(secondary_diagonal)
#
# print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
# print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")

n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

