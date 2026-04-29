class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        t_collection, window = {}, {}

        for char in t:
            # add 1 to existing key
            t_collection[char] = 1 + t_collection.get(char, 0)
        print(t_collection)
        
        have, need = 0, len(t_collection)
        res, smallest_len = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_collection and window[c] == t_collection[c]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < smallest_len:
                    # print(s[l:r+1])
                    res = [l, r]
                    smallest_len = r - l + 1

                # pop the most left position from window
                window[s[l]] -= 1
                if s[l] in t_collection and window[s[l]] < t_collection[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if smallest_len != float("inf") else ""
        