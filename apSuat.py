from decimal import *
import decimal
psi=Decimal(input())
getcontext().prec=6
kgcm2=Decimal(psi*Decimal( 0.453592/(2.54**2)))
print(kgcm2.normalize())