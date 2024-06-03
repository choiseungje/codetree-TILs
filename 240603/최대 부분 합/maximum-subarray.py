a = input()
b = list(map(int,input().split()))
count = 0
lst = []
for i in b:
    if i >= 0:
        count += i
    else:
        lst.append(count)
        count = 0
lst.append(count)
if max(lst) ==  0:
    print(max(b))
else:
    print(max(lst))