a = input()
b = list(map(int,input().split()))
count = 0
if max(b) < 0:
    count = max(b)
for i in b:
    if i >= 0:
        count += i
print(count)