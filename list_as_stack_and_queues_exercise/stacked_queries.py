number = int(input())
numbers = []
for num in range(number):
    command = input().split()
    if command[0] == "1":
        numbers.append(int(command[-1]))
    elif command[0] == "2" and numbers:
        numbers.pop()
    elif command[0] == "3" and numbers:
        print(max(numbers))
    elif command[0] == "4" and numbers:
        print(min(numbers))

numbers = list(map(str, numbers))
numbers = reversed(numbers)
print(f"{', '.join(numbers)}")