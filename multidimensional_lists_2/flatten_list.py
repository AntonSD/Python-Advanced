sub_list = input().split("|")

result = []

for idx in range(len(sub_list) -1, -1, -1):
    current_element = sub_list[idx].strip().split()
    result.extend(current_element)

print(*result, sep=" ")