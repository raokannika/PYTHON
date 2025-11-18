# Program 12: GCD & LCM of two numbers

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = math.gcd(a, b)
l = (a * b) // g

print("GCD:", g)
print("LCM:", l)
