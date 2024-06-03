a = input()
b = list(map(int,input().split()))
count = 0
lst = []
for i in b:
    if max(b) < 0:
        count = max(b)
        break
    if i >= 0:
        count += i
    else:
        lst.append(count)
        count = 0
print(count)