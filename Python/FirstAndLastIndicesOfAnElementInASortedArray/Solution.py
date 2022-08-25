def getRange(arr, target):
    lowestIndex = -1
    highestIndex = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            if lowestIndex == -1:
                lowestIndex = i
            highestIndex = i
        if arr[i] > target:
            break
    
    return [lowestIndex, highestIndex]
            
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(getRange(arr, x))
# [1, 4]

arr = [] 
x = 2
print(getRange(arr, x))
#[-1, -1]

arr = [1, 2, 2, 2, 2, 4, 7, 8, 8] 
x = 3
print(getRange(arr, x))
#[-1, -1]

arr = [1,1,1,1,1,1,1] 
x = 1
print(getRange(arr, x))
#[0, 6]

arr = [1,3,3,5,7,9,15] 
x = 15
print(getRange(arr, x))
#[6, 6]