n, m = [int(el) for el in input().split()]
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(int(input()))
for _ in range(m):
    m_set.add(int(input()))

set_of_elements = n_set.intersection(m_set)
for el in set_of_elements:
    print(el)

    