class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_store = {}
        t_store = {}

        for c_s in s:
            if c_s not in s_store:
                s_store[c_s] = 0
            s_store[c_s] += 1
        
        for c_t in t:
            if c_t not in t_store:
                t_store[c_t] = 0
            t_store[c_t] += 1

        return s_store == t_store