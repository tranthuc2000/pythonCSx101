def calN(n):
  i=0
  while(n>0):
    n=n//10
    i+=1
  return i
def checkAmstrongNumber(x):
  n=calN(x)
  T=0
  m=x
  while(m>0):
    T+=(m%10)**n
    m=m//10
  return(True if T==x else False)


x = 153
result = checkAmstrongNumber(x)
print(result)