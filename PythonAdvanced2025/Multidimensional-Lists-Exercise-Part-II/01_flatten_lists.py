txt = input().split("|")

matrix = []

for i in range(len(txt) - 1, -1, -1):
    row = txt[i].split()
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=" ")