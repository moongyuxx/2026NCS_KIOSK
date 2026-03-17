import numpy as np

items = [48, 7, 99, -3]
items = list(map(lambda i: i+5, items))
print(items)

items = [i+5 for i in items]
print(items)

a = np.array([1, 2, 3, 4, 5])

print(a + 5)
print(a.item(0))