a = [-1, -8, 0, 1, 5]

g = []

for j in a:
    if j >= 1:
        g.append(1)
    elif j <= -1:
        g.append(-1)
    else:
        g.append(0)

print(g)