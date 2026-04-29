class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for c in s:
            if c not in s_count:
                s_count[c] = 0
            s_count[c] += 1
        
        for c in t:
            if c not in t_count:
                t_count[c] = 0
            t_count[c] += 1

        return s_count == t_count