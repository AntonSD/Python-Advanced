rows_of_matrix = int(input())

result = []
matrix = []
for row in range(rows_of_matrix):
    matrix.append([int(x) for x in input().split(", ")])

for j in matrix:
    for k in j:
        result.append(k)
print(result)