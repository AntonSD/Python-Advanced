from collections import deque


def best_list_pureness(numbers, k):
    data = {}
    nums = deque(numbers)

    for rotation in range(k + 1):
        result = sum([index * number for index, number in enumerate(nums)])
        data.update({rotation: result})
        nums.appendleft(nums.pop())
    max_pureness = max(data.values())
    for key, value in data.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
