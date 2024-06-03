a = input()
b = list(map(int,input().split()))
count = 0
for i in b:
    if i >= 0:
        count += i
print(count)