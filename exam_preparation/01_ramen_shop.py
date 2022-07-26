from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while customers and bowls_of_ramen:

    bowl_of_ramen = bowls_of_ramen[-1]
    customer = customers[0]

    if bowl_of_ramen == customer:
        bowls_of_ramen.pop()
        customers.popleft()

    elif bowl_of_ramen > customer:
        bowls_of_ramen[-1] -= customer
        customers.popleft()


    elif customer > bowl_of_ramen:
        bowls_of_ramen.pop()
        customers[0] -= bowl_of_ramen

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
elif not bowls_of_ramen and customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
