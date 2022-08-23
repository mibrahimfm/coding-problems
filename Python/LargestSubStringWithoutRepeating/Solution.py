class Solution:
  def lengthOfLongestSubstring(self, s):
      n = len(s)
      largestSubstring = 0
      currentSubstring = 0
      substring = ""
      charsInSubstring = {}
      for i in range(n):
          c = s[i]
          indexCharInSubstring = substring.find(c)
          print(substring, c, indexCharInSubstring)
          if indexCharInSubstring != -1:
            substring = substring[indexCharInSubstring+1:]
            currentSubstring = len(substring)
          substring += c
          currentSubstring += 1
          if currentSubstring > largestSubstring:
            largestSubstring = currentSubstring
      return largestSubstring
          
              

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10