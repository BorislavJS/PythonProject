n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(num) for num in first_range.split(",")]
    second_start, second_end = [int(num) for num in second_range.split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_list = sorted(longest_intersection)
print(f"Longest intersection is {longest_list} with length {len(longest_intersection)}")

