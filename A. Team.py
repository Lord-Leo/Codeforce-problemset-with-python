n=int(input())
per=0
for _ in range(n):
    x,y,z = map(int, input().split())         #you can take multiple input just like cin >>x>>y>>z
    if((x+y+z)>=2):
        per=per+1
print(per)