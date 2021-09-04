import math
def checkFibonaciNumber(n):
  return( True if checkPerfectSquare(n)== True else False)
def checkPerfectSquare(n):
  return(True if(int(math.sqrt(n))==math.sqrt(n)) else False)
n = 21
result = checkFibonaciNumber(n)
print(result) 