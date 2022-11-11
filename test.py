x = ['a', 'b', 'c', 'd', 'e', 'f','g']
def testing(x):
    a = []
    b = []
    c = []
    for i in range(len(x)):
        if i%3 == 0:
            a.append(x[i])
        if i%3 == 1:
            b.append(x[i])
        if i%3 == 2:
            c.append(x[i])
    return [a, b, c]
print(testing(x))