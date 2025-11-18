# Program 3: Factorial using Loop

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)

# Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial (recursion) of", n, "is", factorial(n))

# Explanation:
# Factorial(n) = n * (n-1) * (n-2) ... * 1
