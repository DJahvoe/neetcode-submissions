class Solution:
    def isCollectionSame(self, t_collection, temp_collection):
        for key in t_collection:
            if t_collection[key] > temp_collection[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        
        result = ''
        smallest_substring_len = float("inf")

        t_collection = {}
        temp_collection = {}

        # count the target of substring
        for i in t:
            if i not in t_collection:
                # initiate both target and temp collection
                t_collection[i] = 0
                temp_collection[i] = 0
            t_collection[i] += 1
        
        while r < len(s):
            char = s[r]
            if char in temp_collection:
                temp_collection[char] += 1
            
            # try to shrink window if all characters in `t` are satisfied
            while self.isCollectionSame(t_collection, temp_collection):
                temp_result = s[l:r+1]
                if smallest_substring_len > len(temp_result):
                    smallest_substring_len = len(temp_result)
                    result = temp_result
                
                if s[l] in temp_collection:
                    temp_collection[s[l]] -= 1
                l += 1
            r += 1
            
        return result
        