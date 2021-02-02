
def search(nums,n):
    l = 0
    u = len(nums)-1

    while l <= u:
        mid = (l+u)//2

        if nums[mid] == n:
            return True
        else:
            if nums[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

nums = [23,25563,653,233,101,54536,6346]
n = 233

if search(nums,n):
    print("Found")
else:
    print("Not Found")

