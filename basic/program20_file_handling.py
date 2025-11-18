# Program 20: File read and write

# Write to file
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.\nWelcome to Python!")

# Read file
with open("sample.txt", "r") as f:
    content = f.read()

print("File content:\n", content)
