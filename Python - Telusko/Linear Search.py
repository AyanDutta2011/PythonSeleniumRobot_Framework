#for linear search values can be unordered

pos = -1      #global variable

def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i    #making global variable from local variable
            return True
        i += 1
    return False

list = [5, 3, 8, 6, 9, 10, 18]
n = 9

if search(list, n):
    print("Found at:", pos+1)
else:
    print("Not found in the list")