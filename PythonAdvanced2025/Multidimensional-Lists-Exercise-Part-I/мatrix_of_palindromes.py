# rows, columns = [int(el) for el in input().split()]
#
# for row in range(rows):
#     matrix = []
#     for col in range(columns):
#         first_and_last = chr(ord("a") + row)
#         middle = chr(ord("a") + row + col)
#         palindrome = first_and_last + middle + first_and_last
#         matrix.append(palindrome)
#     print(" ".join(matrix))

rows, cols = [int(x) for x in input().split()]

start = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(start + row)}{chr(start +row + col)}{chr(start + row)}", end=" ")
    print()