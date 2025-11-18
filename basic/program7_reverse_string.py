# Program 7: Reverse a string manually

text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

print("Reversed string:", rev)

# Explanation:
# We build the reversed string by adding characters one by one at the front.
