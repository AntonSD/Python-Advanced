from collections import deque

expression = input()
stack = []
balanced = True
for paren in expression:
    if paren in "[{(":
        stack.append(paren)
    elif paren in "]})":
        opening_paren = stack.pop()
        if paren == ']' and opening_paren == '[':
            continue
        elif paren == '}' and opening_paren == '{':
            continue
        elif paren == ')' and opening_paren == '(':
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")