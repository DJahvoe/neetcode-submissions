import math

class Solution:
    def isPalindrome(self, arr):
        if len(arr) == 1:
            return True
        mid = math.ceil(len(arr) / 2)
        for i in range(mid):
            j = len(arr) - i - 1
            if arr[i] != arr[j]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                cur = s[i:j+1]
                if self.isPalindrome(cur) and len(cur) > len(res):
                    res = cur
        return res

