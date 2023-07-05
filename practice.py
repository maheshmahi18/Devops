x,y=map(str,input().split())
y=int(y)
l=len(x)
b=0;c=y
for i in range(l//y):
    a=x[b:c]
    print(a[len(a)-1],end="")
    for i in range(1,len(a)-1):
        print(a[i],end="")
    print(a[0],end="")
    b+=y;c+=y