def stats(*args):
    positive = sum([x for x in args if x > 0])
    negative = sum([x for x in args if x < 0])

    result = f"{negative}\n{positive}\n"

    if abs(negative) > positive:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"
    return  result

numbers = [int(x) for x in input().split()]
print(stats(*numbers))