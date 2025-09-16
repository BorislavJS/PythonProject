n, m = map(int, input().split())

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(int(input()))

for _ in range(m):
    second_set.add(int(input()))

common_elements = first_set & second_set

for num in common_elements:
    print(num)