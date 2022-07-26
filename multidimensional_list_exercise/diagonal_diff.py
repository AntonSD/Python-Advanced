number = int(input())
matrix = []
for _ in range(number):
    matrix.append([int(el) for el in input().split(" ")])

first_diagonal_sum = 0
second_diagonal_sum = 0
for row in range(len(matrix)):
    first_diagonal_sum += matrix[row][row]

for col in range(len(matrix) - 1, -1, -1):
    second_diagonal_sum += matrix[len(matrix)-1 - col][col]

difference = abs(first_diagonal_sum - second_diagonal_sum)
print(difference)