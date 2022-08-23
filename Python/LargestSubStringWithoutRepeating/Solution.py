class Solution:
  def lengthOfLongestSubstring(self, s):
      n = len(s)
      largestSubstring = 0
      currentSubstring = 0
      charsInSubstring = {}
      for i in range(n):
          c = s[i]
          if c in charsInSubstring:
            charsInSubstring = {key:value for key, value in charsInSubstring.items() if value > i}
            currentSubstring = len(charsInSubstring)
          
          charsInSubstring[c] = i
          currentSubstring += 1
          if currentSubstring > largestSubstring:
            largestSubstring = currentSubstring
      return largestSubstring
              

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10