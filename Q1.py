n = int(input())
stock_str = input().split(' ')
stock = [x for x in stock_str]
m = int(input())
required_str = input().split(' ')
required = [x for x in required_str]
stock_trash = stock
if n < m:
    print('No')

# print(stock)
# for checking the exact same size
for i in stock:
    if i in required:
        required.remove(i)
new = []

# check for the larger size (L) All XL -> L
for i in stock:
    x = i.replace("X", '')
    if x != 'S':
        new.append(i.replace('X', ''))
for i in new:
    if i in required:
        required.remove(i)
#print(stock)
# print(required)

# Check for M
#Change required M to L
new_required = required
for i in new_required:
    if i =='M':
        required.remove(i)
        required.append('L')
for i in new:
     if i in required:
        required.remove(i)

# return yes or no
if m > 0 and len(required) == 0:
    print('Yes')
else:
    print('No')