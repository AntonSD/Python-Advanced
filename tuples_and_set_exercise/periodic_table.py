number_of_sets = int(input())
unique_elements = set()

for _ in range(number_of_sets):
    list_of_elements = input().split()
    for el in list_of_elements:
        unique_elements.add(el)

for el in unique_elements:
    print(el)