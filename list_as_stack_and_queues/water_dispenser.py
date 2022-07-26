from collections import deque

litters = int(input())

name = input()
queue = deque()
while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.startswith("refill"):
        litters += int(command.split()[-1])
    else:
        litters_wanted = int(command)
        name = queue.popleft()
        if litters_wanted <= litters:
            litters -= litters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait" )

    command = input()
print(f"{litters} liters left")