# Program 14: Check Armstrong number

num = int(input("Enter a number: "))
s = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    s += digit ** n
    temp //= 10

if s == num:
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")
