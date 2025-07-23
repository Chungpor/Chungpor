a = float (input("Enter A value :"))
b = float (input("Enter B value:"))
c =float (input ("Enter C value:"))
d =float (input ("Enter D value :"))
s = (a + b + c + d) /2
area = (s * (s -a )*( s-b )*(s-c)*(s-d))**0.5
print ("the area of triangle is %0.2f"%area)