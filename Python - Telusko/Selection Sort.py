# here we will find min or max value

def sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j

        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp
        print(nums)

nums = [6, 2, 4, 9, 8, 12, 76, 34, 89, 102, 99, 19]
sort(nums)
print("Final Value: ",nums)


