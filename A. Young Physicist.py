n = int(input())
sumx = sumy = sumz = 0
for _ in range(n):
    x, y, z = map(int, (input()).split())
    sumx+=x
    sumy+=y
    sumz+=z
if sumx==sumy==sumz==0:
    print("YES")
else:
    print("NO")