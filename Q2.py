n = int(input())
errorCodes = []
for i in range(n):
    x_str = input().split(' ')
    x = [i for i in x_str]
    if 'false' in x:
        errorCodes.append(x[2])

if n > 0 and len(errorCodes) == 0:
    print("Yes")
else:
    print('No')
    print(*errorCodes, sep= " ")