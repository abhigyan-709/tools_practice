a = [1, 2, 3, [1, 2, 4], [1,1,1]]
b = []
for i in range(a):
    a.extend(i)
    b.append(b)

print(b)