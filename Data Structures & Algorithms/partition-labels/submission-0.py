class Solution:

    def isOverlap(self, s1, e1, s2, e2):
        return not (e1 < s2 or e2 < s1)

    def partitionLabels(self, s: str) -> List[int]:
        char_interval = {}

        # set first and last
        for i in range(len(s)):
            if s[i] not in char_interval:
                char_interval[s[i]] = [-1, -1]

            if char_interval[s[i]][0] == -1:
                char_interval[s[i]][0] = i
                char_interval[s[i]][1] = i
                continue
            char_interval[s[i]][1] = i
        
        # merge overlap
        interval_val = char_interval.values()
        iv = list(interval_val)
        print(interval_val)
        no_overlap_interval = []

        i = 0
        while i < len(iv):
            print(i)
            cur = [iv[i][0], iv[i][1]]

            while i < len(iv) - 1 and self.isOverlap(cur[0], cur[1], iv[i + 1][0], iv[i + 1][1]):
                cur = [min(cur[0], iv[i + 1][0]), max(cur[1], iv[i + 1][1])]
                i += 1

            no_overlap_interval.append(cur[1] - cur[0] + 1)
            i += 1
        
        return no_overlap_interval

