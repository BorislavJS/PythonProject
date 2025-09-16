n = int(input())
unique_name = set()

for _ in range(n):
    name = input()
    unique_name.add(name)

for name in unique_name:
    print(name)

