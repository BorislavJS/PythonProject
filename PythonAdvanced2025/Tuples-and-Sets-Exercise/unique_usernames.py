n = int(input())
unique_name = set()

for _ in range(n):
    names = input()
    unique_name.add(names)

for name in unique_name:
    print(name)