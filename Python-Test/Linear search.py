
def search(nums,n):
    i = 0

    while i < len(nums):
        if nums[i] == n:
            return True
        i = i+1
    return False

nums = [23,25563,653,233,101,54536,6346]
n = 101

if search(nums,n):
    print("Found")
else:
    print("Not Found")


