n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    code = input()
    if code[0].isdigit():
        vip_guests.add(code)
    else:
        regular_guests.add(code)

while True:
    guest = input()
    if guest == "END":
        break
    vip_guests.discard(guest)
    regular_guests.discard(guest)

remaining_guest = sorted(vip_guests) + sorted(regular_guests)
print(len(remaining_guest))
for guest in remaining_guest:
    print(guest)