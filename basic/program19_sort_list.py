# Program 19: Sort a list manually (Bubble Sort)

nums = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("Sorted list:", nums)
