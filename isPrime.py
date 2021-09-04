import math
def checkPrimeNumber(n):
   if(n<=3):
     return True
   i=4
   while(i<=math.sqrt(n)):
      if(n%i==0):
        return False
        i+=1
   return True
n=int(input())
print(checkPrimeNumber(n))
