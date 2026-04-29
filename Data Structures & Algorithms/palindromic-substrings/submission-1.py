class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        strlen = len(s)
        # odd palindrome
        print("ODD")
        for i in range(strlen):
            print(s[i])
            l = r = i
            while(l >= 0 and r < strlen):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
            
        # even palindrome
        print("EVEN")
        for j in range(strlen):
            print(s[j])
            l, r = j, j + 1
            while(l >= 0 and r < strlen):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
        
        return total
