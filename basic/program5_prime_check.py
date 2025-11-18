# Program 5: Check Prime Number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime")
            break
    else:
        print(num, "is Prime")
else:
    print("Number should be greater than 1")

# Explanation:
# A prime number has only two factors: 1 and itself.
