# Program 9: Sum of digits of a number

num = int(input("Enter a number: "))
s = 0

while num > 0:
    s += num % 10
    num //= 10

print("Sum of digits:", s)

# Explanation:
# Take last digit using num % 10, then remove it using num //= 10.
