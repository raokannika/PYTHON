# Remove duplicates while keeping order

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    if x not in lst:
        lst.append(x)

print("List after removing duplicates:", lst)

