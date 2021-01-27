# bubble sort use swaping method

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [6, 2, 4, 9, 8, 12, 76, 34, 89, 102, 99, 19]
sort(nums)
print(nums)