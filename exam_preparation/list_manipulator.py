from collections import deque


def list_manipulator(*args):
    manipulation_list = list(deque(args[0]))
    command = args[1]
    if command == "add":
        if args[2] == "beginning":
            if args[3]:
                manipulation_list.appendleft(args[3:])
            return manipulation_list
        if args[2] == 'end':
            if args[3]:
                manipulation_list.append(args[3:])
            return manipulation_list
    elif command == "remove":
        pass


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
