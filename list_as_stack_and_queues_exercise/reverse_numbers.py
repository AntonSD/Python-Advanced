numbers = input().split()
reversed_number = []
for i in range(len(numbers)):
    reversed_number.append(numbers.pop())

print(" ".join(reversed_number))