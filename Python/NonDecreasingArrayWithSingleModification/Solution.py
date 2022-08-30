def check(lst):
    counter = 0

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            counter += 1
    return not counter > 1

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False
print(check([3,3,3,3,3]))
# True
print(check([1,2,4,8,16]))
# True
print(check([2,1,4,3,4]))
# False
print(check([5,3,1]))
# False