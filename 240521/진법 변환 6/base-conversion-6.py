k = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a,b,c = input().split()
sum = 0
for i in range(len(b)):
    sum += int(b[i]) * int(a)**(len(b)-i-1)
answer = ''
while sum > 0:
    answer = k[sum%int(c)] + answer
    sum //= int(c)
print(answer)