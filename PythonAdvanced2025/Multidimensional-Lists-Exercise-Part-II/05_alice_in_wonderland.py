n = int(input())

matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

moves = {"down": (1, 0), "up": (-1, 0), "right": (0, 1), "left": (0, -1)}
tea_bags = 0

while tea_bags < 10:
    direction = input()
    move = moves[direction]
    r = alice[0] + move[0]
    c = alice[1] + move[1]

    if  r < 0 or r >= n or c < 0 or c >= n:
        break
    if matrix[r][c] == "R":
        matrix[r][c] = "*"
        break

    if matrix[r][c] not in "*.":
        tea_bags += int(matrix[r][c])

    matrix[r][c] = "*"
    alice = [r, c]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]