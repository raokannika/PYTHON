# Program 8: Count vowels and consonants

text = input("Enter a string: ").lower()
vowels = "aeiou"

v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count, "Consonants:", c_count)

# Explanation:
# Check each character, if it's alphabet then count vowels & consonants separately.
