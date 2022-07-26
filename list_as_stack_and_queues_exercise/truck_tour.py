from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for i in range(n):
    fuel_tank = 0
    current_gas_pump = 0
    for gas_pump in queue:
        fuel = gas_pump[0]
        distance_to_next = gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        current_gas_pump += 1
    if current_gas_pump:
        print(current_gas_pump)
    queue.rotate(-1)

