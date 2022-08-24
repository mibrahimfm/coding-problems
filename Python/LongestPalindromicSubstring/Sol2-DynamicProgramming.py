def longestPalindrome(s):
    n = len(s)
    
    palindromeMatrix = [[False for x in range(n)] for y in range(n)]
    for i in range(n):
        palindromeMatrix[i][i] = True
    
    startingIndex = 0
    lengthLongestPalindrome = 1
        
    for i in range(n-1):
        if s[i] == s[i+1]:
            palindromeMatrix[i][i+1] = True
            startingIndex = i
            lengthLongestPalindrome = 1
    
    for i in range(3, n+1):
        for j in range (n-i+1):
            k = i + j - 1
            if palindromeMatrix[j+1][k-1] and s[j] == s[k]:
                palindromeMatrix[j][k] = True
                startingIndex = j
                lengthLongestPalindrome = i
    
    return s[startingIndex:startingIndex+lengthLongestPalindrome]       
    
        
        
    
# Test program

print(str(longestPalindrome("socorrammesubinoonibusemmarrocos")))
#socorrammesubinoonibusemmarrocos
print(str(longestPalindrome("abdssdiiasd")))
#dssd
print(str(longestPalindrome("tracecare")))
# racecar
print(str(longestPalindrome("abcdefghijklmnopqrstuvwxyz")))
#a
print(str(longestPalindrome("forgeeksskeegfor")))