number = int(input())

usernames = set()

for _ in range(number):
    usernames.add(input())

for name in usernames:
    print(name)