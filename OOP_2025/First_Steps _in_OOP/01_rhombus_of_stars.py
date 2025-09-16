
def upper_part(n):
    for row in range(1, n + 1):
        print(f"{' ' * (n - row)} {'* ' * row} ")

def bottom_part(n):
    for row in range(1, n):
        print(f"{' ' * row} {'* ' * (n - row)}")

n = int(input())
upper_part(n)
bottom_part(n)