def lengthOfLongestSubstring(s):
    n = len(s)
    if n == 0:
      return -1
    
    if n == 1:
      return 1
    
    largestSubstring = 0
    currentSubstring = 0
    charsInSubstring = {}
    
    for i in range(n):
        c = s[i]
        if c in charsInSubstring:
          charsInSubstring = {key:value for key, value in charsInSubstring.items() if value > charsInSubstring[c]}
          currentSubstring = len(charsInSubstring)
        
        charsInSubstring[c] = i
        currentSubstring += 1
        if currentSubstring > largestSubstring:
          largestSubstring = currentSubstring
          
    return largestSubstring
              
print(lengthOfLongestSubstring('geeksforgeeks')) 
#7
print(lengthOfLongestSubstring('aabrakkaershaopgdysyyys')) 
#10
print(lengthOfLongestSubstring('abrkaabcdefghijjxxx')) 
#10
print(lengthOfLongestSubstring('')) 
# #-1
print(lengthOfLongestSubstring('a')) 
# #1
print(lengthOfLongestSubstring('aaaaaaaaaaaaaaaaaaaaaaaaaaa')) 
# #1
print(lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyz')) 
# #26
print(lengthOfLongestSubstring('aaaabaaaa')) 
# #2