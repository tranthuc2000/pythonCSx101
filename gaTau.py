k,t=list(map(int,input().split()))
if((t//k)%2==0 and t%k==0):
    print(0)
elif((t//k)%2==1 and t%k==0):
    print(k)
elif((t//k)%2==0 and t%k!=0):
    print(t%k)
else:
    print(k-(t%k))