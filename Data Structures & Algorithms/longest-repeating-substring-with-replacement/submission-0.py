class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = {}
        res = 0
        for r in range(len(s)):
            print(charCount)
            # add character to charCount
            if s[r] in charCount:
                charCount[s[r]] += 1
            else:
                charCount[s[r]] = 1
            
            # get most frequent
            maxf = 0
            for char in charCount:
                maxf = max(maxf, charCount[char])
            
            # if replacable is >= k (invalid), decrement s[l] counts, and add + 1 to l
            while (r - l + 1) - maxf > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
                
