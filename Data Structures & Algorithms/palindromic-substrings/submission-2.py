class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        strlen = len(s)
        # odd palindrome
        for i in range(strlen):
            l = r = i
            while(l >= 0 and r < strlen):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
            
        # even palindrome
        for j in range(strlen):
            l, r = j, j + 1
            while(l >= 0 and r < strlen):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
        
        return total
