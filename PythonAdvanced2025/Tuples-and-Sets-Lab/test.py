n = int(input())
coordinates = set()

for _ in range(n):
    x , y = map(int, input().split())
    coordinates.add((x, y))

print(len(coordinates))