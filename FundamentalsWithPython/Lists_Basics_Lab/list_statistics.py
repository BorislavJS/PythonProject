# n = int(input())
#
# positive = []
# negative = []
#
# for _ in range(n):
#     number = int(input())
#
#     if number >= 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print(positive)
# print(negative)
# print(f"Count of positives: {len(positive)}")
# print(f"Sum of negatives: {sum(negative)}")

n = int(input())

positive = []
negative = []
count = 0
sum_negative = 0
for _ in range(n):
    number = int(input())

    if number >= 0:
        positive.append(number)
        count += 1
    else:
        negative.append(number)
        sum_negative += number

print(positive)
print(negative)
print(f"Count of positives: {count}")
print(f"Sum of negatives: {sum_negative}")

