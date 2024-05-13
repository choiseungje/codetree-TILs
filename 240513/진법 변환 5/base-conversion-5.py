a,b = map(int,input().split())
lst=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
lst = lst[:b+1]
answer = ''
while a >0:
    answer = lst[a%b]+answer
    a //= b
print(answer)