num = int(input())

reservatioins = set()
for _ in range(num):
    ticket = input()
    reservatioins.add(ticket)

guest = input()
while not guest == "END":
    reservatioins.remove(guest)
    guest = input()

print(len(reservatioins))
for guest in sorted(reservatioins):
    if guest[0].isdigit():
        print(guest)
for guest in sorted(reservatioins):
    if guest[0].isalpha():
        print(guest)