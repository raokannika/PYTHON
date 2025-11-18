# Program 18: Count word frequency using dictionary

text = "this is a test this is only a test"
words = text.split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
