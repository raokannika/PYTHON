# Program 6: Check if a string is Palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")

# Explanation:
# A palindrome reads the same forwards and backwards.
