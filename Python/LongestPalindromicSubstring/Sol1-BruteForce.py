def getAllSubstring(s):
    subStrings = {}
    for i in range(len(s)):
        subStr = ""
 
        # Second loop is generating sub-String
        for j in range(i,len(s)):
            subStr += s[j]
            subStrings[subStr] = len(subStr)
        
    sortedSubStirngs = [key for key, _ in sorted(subStrings.items(), key=lambda x : x[1], reverse=True)]
    return sortedSubStirngs

def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

def longestPalindrome(s):
    substrings = getAllSubstring(s)
    
    for ss in substrings:
        if isPalindrome(ss):
            return ss
        
    return ""

        
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