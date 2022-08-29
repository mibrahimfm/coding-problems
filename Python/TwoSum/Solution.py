def two_sum(arr, target):
    complements = set()
    
    for i in arr:
        if i in complements:
            return True
        complements.add(target - i)
    
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
print(two_sum([4,7,-3,2], 5))
# False
print(two_sum([], 5))
# False
print(two_sum([], 0))
# False
print(two_sum([3, 2, 4, 3], 4))
# False
print(two_sum([3, 2, 4, 0], 4))
# True