#binary search is faster than linear search
# values should be in sorted format

pos = -1      #global variable

def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid  # making global variable from local variable
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid + 1


list = [5, 7, 8, 16, 29, 30, 123, 456, 678, 700, 800, 12467, 123455, 123456456]
n = 123

if search(list, n):
    print("Found at:", pos+1)
else:
    print("Not found in the list")