divisor = int(input())
boundary = int(input())

result = 0
sum_result = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        result = num
        sum_result += num

print(result)
print(sum_result)





