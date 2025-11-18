# Second largest element in list

lst = list(map(int, input("Enter numbers: ").split()))
unique = list(set(lst))   # remove duplicates
unique.sort()             # sort in ascending order

if len(unique) < 2:
    print("Second largest does not exist")
else:
    print("Second largest:", unique[-2])
