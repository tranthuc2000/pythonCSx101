import math
a,b,c=list(map(float,input().split()))
print(format(a**5-2*math.sqrt(abs(b))+a*b*c,".2f"))