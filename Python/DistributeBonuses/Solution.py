def getBonuses(performance):
    n = len(performance)
    bonuses = [1 for _ in range(n)]
    
    for i in range(n):
        if i+1 < n:
            if performance[i] > performance[i+1]:
                bonuses[i] += 1
            elif performance[i] < performance[i+1]:
                bonuses[i+1] += 1
                
    return bonuses

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
print(getBonuses([9]))
#[1]
print(getBonuses([3, 2, 3, 3, 4, 5, 4]))
#[2, 1, 2, 1, 2, 3, 1]