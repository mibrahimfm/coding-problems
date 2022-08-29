def singleNumber(nums):
    duplicates = {}
    
    for n in nums:
        if n in duplicates:
            duplicates[n] = True
        else:
            duplicates[n] = False
    
    nonDuplicateNumber = [key for key, val in duplicates.items() if val == False]
    
    return nonDuplicateNumber[0]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
print(singleNumber([4, 3, 2, 4, 1, 3, 2, 1, 6, 9, 13, 13, 9]))
# 6