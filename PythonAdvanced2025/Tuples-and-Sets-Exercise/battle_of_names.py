n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(ch) for ch in name)
    result = ascii_sum // row

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result_set = odd_set | even_set
elif sum_odd > sum_even:
    result_set = odd_set - even_set
else:
    result_set = odd_set ^ even_set

print(", ".join(str(x) for x in result_set))

