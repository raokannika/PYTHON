# Program 4: Fibonacci sequence up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Explanation:
# Each term is the sum of the previous two terms.
# Starts with 0 and 1.
