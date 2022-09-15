def witnesses(heights):
    maxHeight = 0
    witnessesCount = 0
    for i in reversed(range(len(heights))):
        if heights[i] > maxHeight:
            witnessesCount += 1
            maxHeight = heights[i]
    return witnessesCount        

print(witnesses([3, 6, 3, 4, 1]))
# 3

print(witnesses([7, 6, 5, 4, 1]))
#5

print(witnesses([1, 2, 3, 4, 5]))
#1

print(witnesses([5, 5, 5, 5, 5]))
#1