from collections import deque

eggs = deque(int(x) for x in input().split(", ") if int(x) > -101 and int(x) < 101)
papers = deque(int(x) for x in input().split(", ") if int(x) >= 1 and int(x) < 101)

boxes = 0

while eggs and papers:
    egg = eggs[0]
    paper = papers[-1]
    if egg <= 0:
        eggs.popleft()
        continue
    if egg == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    if egg + paper <= 50:
        eggs.popleft()
        papers.pop()
        boxes += 1
    else:
        eggs.popleft()
        papers.pop()

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
