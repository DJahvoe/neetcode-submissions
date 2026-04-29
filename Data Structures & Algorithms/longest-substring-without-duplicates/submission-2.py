class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charList = set()
        maxLen = 0
        while r < len(s):
            print(charList)
            while s[r] in charList:
                charList.remove(s[l])
                l += 1
            charList.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
