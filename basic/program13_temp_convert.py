# Program 13: Temperature conversion

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("In Fahrenheit:", f)

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print("In Celsius:", c)
