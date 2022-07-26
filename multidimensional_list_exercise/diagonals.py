number = int(input())
matrix = []
for _ in range(number):
    matrix.append([int(el) for el in input().split(", ")])

first_diagonal_sum = 0
second_diagonal_sum = 0
first_diagonal = []
second_diagonal = []
for row in range(len(matrix)):
    first_diagonal.append(str(matrix[row][row]))
    first_diagonal_sum += matrix[row][row]

for col in range(len(matrix) - 1, -1, -1):
    second_diagonal.append(str(matrix[len(matrix)-1 - col][col]))
    second_diagonal_sum += matrix[len(matrix)-1 - col][col]

print(f"Primary diagonal: {', '.join(first_diagonal)}. Sum: {first_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(second_diagonal)}. Sum: {second_diagonal_sum}")