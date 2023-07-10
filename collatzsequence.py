n=int(input())
list_n=[n]
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*(n)+1
    list_n.append(n)
print(*list_n)