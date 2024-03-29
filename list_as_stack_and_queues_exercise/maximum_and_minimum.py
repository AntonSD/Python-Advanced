from collections import deque

n = int(input())

stack = []
for idx in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))

    elif command[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif command[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == "4":
        if len(stack) > 0:
            print(min(stack))

reversed_stack = []

for i in range(len(stack)):
    reversed_stack.append(stack.pop())
reversed_stack = list(map(str, reversed_stack))
print(", ".join(reversed_stack))