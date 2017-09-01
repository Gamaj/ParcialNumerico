import math
import sys

def f1(x,a,b,c):
	return (a*x**2+b*x+c)

def f2(x,a,b):
	return (2*a*x+b)

#ecuacion a(x**2)+ bx + c
#pedir a b y c

a= float(raw_input(" a: "))
b= float(raw_input(" b: "))
c= float(raw_input(" c: "))

res=(b**2)-4*(a*c)

print ("Raices")

if res<0:
 	l= (-1*b)/(2*a)
	imaginario= math.sqrt(res*(-1)) / 2*a
	print l, ' - ', imaginario, 'i'
	print l, ' + ', imaginario, 'i'
	sys.exit(0)

xn=0.1 
x0=0.0
tol=0.0001 
i=1 

while i >= tol:
	xn=x0-(f1(x0,a,b,c)/f2(x0,a,b)) 
	print xn
	i=(xn-x0)/xn 
	x0=xn




 
